# STANDARD IMPORTS
from http import HTTPStatus
import requests

# THIRD PARTY IMPORTS
from etria_logger import Gladsheim

# PROJECT IMPORTS
from func.src.domain.enums.status_code.enum import InternalCode
from func.src.domain.exceptions.exceptions import InvalidBrOnboardingStep
from func.src.domain.response.model import ResponseModel

result = {'suitability': True,
                     'identifier_data': True,
                     'selfie': True,
                     'complementary_data': True,
                     'document_validator': True,
                     'data_validation': True,
                     'electronic_signature': True,
                     'time_experience': True,
                     'current_step': 'finished'}


class ValidateOnboardingStepsBR:
    BASE_URL = 'https://dev.api.siga.me/router/onboarding_steps_br'

    @classmethod
    def get_onboarding_steps_br(cls, thebes_answer: str):
        headers = {'x-thebes-answer': "{}".format(thebes_answer)}
        steps_us_response = requests.get(cls.BASE_URL, headers=headers)

        response = steps_us_response.json().get("result")

        return response

    @classmethod
    async def onboarding_br_step_validator(cls, thebes_answer: str):
        try:
            # response = cls.get_onboarding_steps_br(thebes_answer=thebes_answer)
            time_experience = result.get("time_experience")

            if not time_experience:
                raise InvalidBrOnboardingStep

        except Exception as error:
            Gladsheim.error(error=error)
            response = ResponseModel(
                result=False,
                success=False,
                code=InternalCode.HTTP_CONNECTION_POLL,
                message="Error On HTTP Request"
            ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
            return response
