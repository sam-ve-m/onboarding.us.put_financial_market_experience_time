

class UpdateMarketTimeExperience:

    @classmethod
    async def update_market_time_experience(cls, payload: dict):

        user_time_experience = payload["time_experience"]
        br_step_validator = UserService.onboarding_us_step_validator(
            payload=payload,
        )
        us_step_validator = ValidateOnboardingStepsUS.onboarding_us_step_validator(payload=payload)
        await asyncio.gather(br_step_validator, us_step_validator)

        (
            sent_to_persephone,
            status_sent_to_persephone,
        ) = await UserService.persephone_client.send_to_persephone(
            topic=config("PERSEPHONE_TOPIC_USER"),
            partition=PersephoneQueue.USER_TRADE_TIME_EXPERIENCE_IN_US.value,
            message=get_user_time_experience_schema_template_with_data(
                time_experience=user_time_experience,
                unique_id=thebes_answer["user"]["unique_id"],
            ),
            schema_name="user_time_experience_us_schema",
        )
        if sent_to_persephone is False:
            raise InternalServerError("common.process_issue")

        unique_id = thebes_answer_user["unique_id"]
        was_updated = await UserRepository.update_one(
            old={"unique_id": unique_id},
            new={
                "external_exchange_requirements.us.time_experience": user_time_experience
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