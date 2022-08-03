# STANDARD IMPORTS
import asyncio

# PROJECT IMPORTS
from src.domain.exceptions.exceptions import UniqueIdWasNotUpdate
from src.domain.models.jwt.models import Jwt
from src.domain.models.time_experience.model import TimeExperienceRequest
from src.repositories.user.repository import UserRepository
from src.services.persephone.service import SendToPersephone
from src.transport.onboarding_steps_br import ValidateOnboardingStepsBR
from src.transport.onboarding_steps_us import ValidateOnboardingStepsUS


class UpdateMarketTimeExperience:

    @classmethod
    async def update_market_time_experience(
            cls,
            jwt_data: Jwt,
            time_experience_request: TimeExperienceRequest
            ):

        br_step_validator = ValidateOnboardingStepsBR.onboarding_br_step_validator(jwt_data=jwt_data)

        us_step_validator = ValidateOnboardingStepsUS.onboarding_us_step_validator(jwt_data=jwt_data)

        await asyncio.gather(br_step_validator, us_step_validator)

        await SendToPersephone.register_user_time_experience_log(
            jwt_data=jwt_data,
            time_experience_request=time_experience_request
        )

        was_updated = await UserRepository.update_user_and_time_experience_(
            jwt_data=jwt_data
        )

        if not was_updated:
            raise UniqueIdWasNotUpdate

        return was_updated
