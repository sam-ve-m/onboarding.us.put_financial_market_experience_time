from func.src.transport.onboarding_steps_br import ValidateOnboardingStepsBR
from func.src.transport.onboarding_steps_us import ValidateOnboardingStepsUS
import asyncio


class UpdateMarketTimeExperience:

    @classmethod
    def __extract_unique_id(cls, jwt_data: dict):
        unique_id = jwt_data.get("x-thebes-answer").get("user").get("unique_id")
        time_experience = jwt_data.get("time_experience")
        return unique_id, time_experience

    @classmethod
    async def update_market_time_experience(cls, jwt_data: dict, thebes_answer: str):
        unique_id, time_experience = cls.__extract_unique_id(jwt_data=jwt_data)

        br_step_validator = ValidateOnboardingStepsUS.onboarding_us_step_validator(thebes_answer=thebes_answer)

        us_step_validator = ValidateOnboardingStepsBR.onboarding_us_step_validator(thebes_answer=thebes_answer)

        await asyncio.gather(br_step_validator, us_step_validator)

        (
            sent_to_persephone,
            status_sent_to_persephone,
        ) = await Persephone.send_to_persephone(
            topic=config("PERSEPHONE_TOPIC_USER"),
            partition=PersephoneQueue.USER_TRADE_TIME_EXPERIENCE_IN_US.value,
            message=get_user_time_experience_schema_template_with_data(
                time_experience=time_experience,
                unique_id=unique_id,
            ),
            schema_name="user_time_experience_us_schema",
        )
        if sent_to_persephone is False:
            raise InternalServerError("common.process_issue")

        was_updated = await UserRepository.update_one(
            old={"unique_id": unique_id},
            new={
                "external_exchange_requirements.us.time_experience": time_experience
            },
        )
        if not was_updated:
            raise InternalServerError("common.unable_to_process")

        user_data = await UserRepository.find_one({"unique_id": unique_id})
        await DriveWealthService.registry_update_client(user_data=user_data)

        return {
            "status_code": status.HTTP_200_OK,
            "message_key": "requests.updated",
        }