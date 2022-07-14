# STANDARD IMPORTS
from http import HTTPStatus
from flask import request, Response, Request, Flask

# THIRD PARTY IMPORTS
from etria_logger import Gladsheim

from func.src.services.jwt_service.service import JWTService
from func.src.transport.onboarding_steps_us import ValidateOnboardingStepsUS

app = Flask(__name__)


@app.route('/update_market_experience_time')
async def update_market_experience_time(
        request_body: Request = request) -> Response:
    thebes_answer = request_body.headers.get("x-thebes-answer")
    jwt_data = await JWTService.decode_jwt_from_request(jwt_data=thebes_answer)
    w8_confirmation_param = W8FormConfirmation(**request_body.json).dict()

    payload = {"x-thebes-answer": thebes_answer}
    payload.update(w8_confirmation_param)
    # service_response


if __name__ == "__main__":
    app.run(debug=True)
