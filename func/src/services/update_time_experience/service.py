# STANDARD IMPORTS
import asyncio

# PROJECT IMPORTS
from func.src.domain.exceptions.exceptions import UniqueIdWasNotUpdate
from func.src.repositories.user.repository import UserRepository
from func.src.services.drive_wealth.service import DriveWealthService
from func.src.services.persephone.service import SendToPersephone
from func.src.transport.onboarding_steps_br import ValidateOnboardingStepsBR
from func.src.transport.onboarding_steps_us import ValidateOnboardingStepsUS


class UpdateMarketTimeExperience:

    @classmethod
    def __extract_unique_id(cls, jwt_data: dict):
        unique_id = jwt_data.get("x-thebes-answer").get("user").get("unique_id")
        time_experience = jwt_data.get("time_experience")
        return unique_id, time_experience

    @classmethod
    async def update_market_time_experience(cls, jwt_data: dict, thebes_answer: str):
        unique_id, time_experience = cls.__extract_unique_id(jwt_data=jwt_data)

        br_step_validator = ValidateOnboardingStepsBR.onboarding_br_step_validator(thebes_answer=thebes_answer)

        us_step_validator = ValidateOnboardingStepsUS.onboarding_us_step_validator(thebes_answer=thebes_answer)

        await asyncio.gather(br_step_validator, us_step_validator)

        await SendToPersephone.register_user_time_experience_log(
            unique_id=unique_id, time_experience=time_experience
        )

        was_updated = await UserRepository.update_one(
            old={"unique_id": unique_id},
            new={
                "external_exchange_requirements.us.time_experience": time_experience
            },
        )
        if not was_updated:
            raise UniqueIdWasNotUpdate

        user_data = await UserRepository.find_one({"unique_id": unique_id})
        await DriveWealthService.registry_update_client(user_data=user_data)

        return {
            "message_key": "requests.updated",
        }
