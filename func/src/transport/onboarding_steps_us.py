# STANDARD IMPORTS
from http import HTTPStatus
import requests

# THIRD PART IMPORTS
from etria_logger import Gladsheim

# PROJECT IMPORTS
from src.domain.enums.status_code.enum import InternalCode
from src.domain.exceptions.exceptions import InvalidUsOnboardingStep
from src.domain.response.model import ResponseModel

result = {'terms': True,
          'user_document_validator': True,
          'politically_exposed': True,
          'exchange_member': True,
          'company_director': True,
          'external_fiscal_tax_confirmation': True,
          'employ': True,
          'time_experience': True,
          'current_step': 'finished'}


class ValidateOnboardingStepsUS:
    BASE_URL = 'https://dev.api.siga.me/router/onboarding_steps_us'

    @classmethod
    def __get_onboarding_steps_us(cls, thebes_answer: str):
        headers = {'x-thebes-answer': "{}".format(thebes_answer)}
        steps_us_response = requests.get(cls.BASE_URL, headers=headers)

        response = steps_us_response.json().get("result")

        return response

    @classmethod
    async def onboarding_us_step_validator(cls, thebes_answer: str):
        try:
            # response = cls.__get_onboarding_steps_us(thebes_answer=thebes_answer)
            time_experience = result.get("time_experience")

            if not time_experience:
                raise InvalidUsOnboardingStep

        except Exception as error:
            Gladsheim.error(error=error)
            response = ResponseModel(
                result=False,
                success=False,
                code=InternalCode.HTTP_CONNECTION_POLL,
                message="Error On HTTP Request"
            ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
            return response
