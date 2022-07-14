import requests

from func.src.domain.exceptions.exceptions import BadRequestError

result = {'result': {'terms': True,
                     'user_document_validator': True,
                     'politically_exposed': True,
                     'exchange_member': True,
                     'company_director': True,
                     'external_fiscal_tax_confirmation': True,
                     'employ': True,
                     'time_experience': True,
                     'current_step': 'finished'},
          'message': 'Success', 'success': True, 'code': 0}


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
        response = cls.__get_onboarding_steps_us(thebes_answer=thebes_answer)
        time_experience = response.get("result").get("time_experience")

        if not time_experience:
            raise BadRequestError("ValidateOnboardingStepsUS.onboarding_us_step_validator::you're not in this step")
