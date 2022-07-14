import requests


class ValidateOnboardingStepsBR:
    BASE_URL = 'https://dev.api.siga.me/router/onboarding_steps_br'

    @classmethod
    def validate_onboarding_steps_us(cls, payload: dict):
        headers = {'x-thebes-answer': "{}".format(payload)}
        auth_response = requests.get(cls.BASE_URL, headers=headers)

        current_step = auth_response.json()

        return current_step




result = {'result': {'suitability': True,
                     'identifier_data': True,
                     'selfie': True,
                     'complementary_data': True,
                     'document_validator': True,
                     'data_validation': True,
                     'electronic_signature': True,
                     'current_step': 'finished'},
          'message': 'Success', 'success': True, 'code': 0}
