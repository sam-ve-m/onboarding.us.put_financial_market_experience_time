import requests

BASE_URL = 'https://dev.api.siga.me/router/onboarding_steps_us'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOiAxNjg3OTYxNDIxLCAiY3JlYXRlZF9hdCI6IDE2NTY0MjU0MjEuNjA5MjYsICJzY29wZSI6IHsidmlld190eXBlIjogImRlZmF1bHQiLCAidXNlcl9sZXZlbCI6ICJjbGllbnQiLCAiZmVhdHVyZXMiOiBbImRlZmF1bHQiLCAicmVhbHRpbWUiXX0sICJ1c2VyIjogeyJ1bmlxdWVfaWQiOiAiNDBkYjdmZWUtNmQ2MC00ZDczLTgyNGYtMWJmODdlZGM0NDkxIiwgIm5pY2tfbmFtZSI6ICJSQVNUMyIsICJwb3J0Zm9saW9zIjogeyJiciI6IHsiYm92ZXNwYV9hY2NvdW50IjogIjAwMDAwMDAxNC02IiwgImJtZl9hY2NvdW50IjogIjE0In0sICJ1cyI6IHsiZHdfYWNjb3VudCI6ICI4OWM2OTMwNC0wMThhLTQwYjctYmU1Yi0yMTIxYzE2ZTEwOWUuMTY1MTUyNTI3NzAwNiIsICJkd19kaXNwbGF5X2FjY291bnQiOiAiTFgwMTAwMDAwMSJ9fSwgImNsaWVudF9oYXNfYnJfdHJhZGVfYWxsb3dlZCI6IHRydWUsICJjbGllbnRfaGFzX3VzX3RyYWRlX2FsbG93ZWQiOiB0cnVlLCAiY2xpZW50X3Byb2ZpbGUiOiAiaW52ZXN0b3IifX0.d-BJu3eRUZPfTYmOADlPunN8p7Lwz2aOfHJUmUUb3ZkL7sKs1RLoyJULIMk7EM8FIIE6-TYxvljQ_TDd_F2dU8LFelHKCbRbhSFZriX3MPKUv_0b0tIheS3k8Og0h4-DRKkWlVDcdTLP8bBmmN1tUmvsU_-BVaJyQX7doh5j__t6t4GeoETc8MoER2jv01MvIB4M8QgFTMKqdozA9G4qBATwfjTJaxDWlR67KEmqilI84BbqBF9zKegkJJwwPALtZ9RYNaXlXPQ4-ZHqz1v6LYPFpO28Rgf6fPTAEbDKaelZ7w7nzXRUyj_rw-YYxCnBnaw7wwLeckEkWgRPO3E60w'


class ValidateOnboardingStepsBR:

    @classmethod
    def validate_onboarding_steps_br(cls):
        headers = {'x-thebes-answer': "{}".format(token)}
        auth_response = requests.get(BASE_URL, headers=headers)

        return auth_response


if __name__ == '__main__':
    response = ValidateOnboardingStepsBR.validate_onboarding_steps_br()
    print(response.json())
