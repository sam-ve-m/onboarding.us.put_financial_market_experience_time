# STANDARD IMPORTS
from unittest.mock import patch, Mock
# import pytest
#
# # PROJECT IMPORTS
# from func.src.transport.onboarding_steps_br import ValidateOnboardingStepsBR
# from func.src.transport.onboarding_steps_us import ValidateOnboardingStepsUS
# from func.src.services.persephone.service import SendToPersephone
# from func.src.services.update_time_experience.service import UpdateMarketTimeExperience
# from src.domain.models.time_experience.model import TimeExperienceRequest
# from src.repositories.user.repository import UserRepository
#
# get_unique_id_from_jwt_payload = "125458.hagfsdsa"
#
#
# @pytest.mark.asyncio
# @patch.object(ValidateOnboardingStepsBR, "validate_onboarding_steps_br", side_effect=[None, None])
# @patch.object(ValidateOnboardingStepsUS, "validate_onboarding_steps_us", side_effect=[None, None])
# @patch.object(SendToPersephone, "register_user_time_experience_log", return_value=None)
# @patch.object(UserRepository, "update_user_and_time_experience", return_value=True)
# async def test_when_sending_right_params_to_update_market_time_experience_then_return_the_expected(
#         mock_onboarding_br_step_validator,
#         mock_onboarding_us_step_validator,
#         mock_register_user_time_experience_log,
#         mock_update_one
# ):
#     response = await UpdateMarketTimeExperience.update_market_time_experience(
#         jwt_data=Mock(return_value=get_unique_id_from_jwt_payload),
#         time_experience_request=TimeExperienceRequest(**{"time_experience": "10"})
#     )
#     assert response is True
#
#
# @pytest.mark.asyncio
# @patch.object(ValidateOnboardingStepsBR, "validate_onboarding_steps_br", side_effect=[None, None])
# @patch.object(ValidateOnboardingStepsUS, "validate_onboarding_steps_us", side_effect=[None, None])
# @patch.object(SendToPersephone, "register_user_time_experience_log", return_value=None)
# @patch.object(UserRepository, "update_user_and_time_experience", return_value=True)
# async def test_when_sending_right_params_to_update_market_time_experience_then_return_the_expected(
#         mock_onboarding_br_step_validator,
#         mock_onboarding_us_step_validator,
#         mock_register_user_time_experience_log,
#         mock_update_one
# ):
#     response = await UpdateMarketTimeExperience.update_market_time_experience(
#         jwt_data=Mock(return_value=get_unique_id_from_jwt_payload),
#         time_experience_request=TimeExperienceRequest(**{"time_experience": "10"})
#     )
#     assert response is True
