# STANDARD IMPORTS
from http import HTTPStatus
import requests

# THIRD PART IMPORTS
from etria_logger import Gladsheim

# PROJECT IMPORTS
from func.src.domain.enums.status_code.enum import InternalCode
from func.src.domain.exceptions.exceptions import InvalidUsOnboardingStep
from func.src.domain.response.model import ResponseModel
from func.src.infrastructure.env_config import config


class ValidateOnboardingStepsUS:
    onboarding_steps_us_url = config("US_BASE_URL")

    @classmethod
    def __get_onboarding_steps_us(cls, thebes_answer: str):
        headers = {'x-thebes-answer': "{}".format(thebes_answer)}
        try:
            steps_us_response = requests.get(cls.onboarding_steps_us_url, headers=headers)

            response = steps_us_response.json().get("result")
            return response

        except Exception as error:
            Gladsheim.error(error=error)
            response = ResponseModel(
                result=False,
                success=False,
                code=InternalCode.HTTP_CONNECTION_POLL,
                message="Error On HTTP Request"
            ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
            return response

    @classmethod
    async def onboarding_us_step_validator(cls, thebes_answer: str):

        response = cls.__get_onboarding_steps_us(thebes_answer=thebes_answer)
        time_experience = response.get("time_experience")

        if not time_experience:
            raise InvalidUsOnboardingStep
