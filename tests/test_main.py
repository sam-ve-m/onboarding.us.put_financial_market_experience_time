# STANDARD IMPORTS
from unittest.mock import patch
import pytest
from flask import Flask
from heimdall_client import HeimdallStatusResponses, Heimdall
from werkzeug.datastructures import Headers

# PROJECT IMPORTS
from func.main import update_experience_time
from func.src.domain.models.jwt.models import Jwt
from func.src.services.update_time_experience.service import UpdateMarketTimeExperience

# STUB IMPORTS
from tests.main_stub import request_body_stub, decoded_jwt_stub

jwt_response = "125458.hagfsdsa"


@pytest.mark.asyncio
@patch.object(Heimdall, "decode_payload", return_value=(decoded_jwt_stub, HeimdallStatusResponses.SUCCESS))
@patch("src.services.enum_experience_time.service.ExperienceTimeEnumService.experience_time_enum_validation", return_value=True)
@patch(
    "src.services.update_time_experience.service.UpdateMarketTimeExperience.update_market_time_experience",
    return_value=True
)
async def test_when_sending_right_params_to_update_market_experience_time_then_return_the_expected(
        mock_update_market_time_experience,
        mock_experience_time_enum_validation,
        mock_decode_and_validate_jwt
):

    app = Flask(__name__)
    with app.test_request_context(
            json=request_body_stub,
            headers=Headers({"x-thebes-answer": "jwt_to_decode_stub"}),
    ).request as request:
        response = await update_experience_time(
            request_body=request
        )
        assert response.status_code == 200

enums_data_stub = [("LALA", 'lala'), ('LILI', 'lili')]


@pytest.mark.asyncio
@patch.object(Heimdall, "decode_payload", return_value=(None, HeimdallStatusResponses.INVALID_TOKEN))
@patch("src.services.enum_experience_time.service.ExperienceTimeEnumService.experience_time_enum_validation", return_value=False)
@patch.object(Jwt, "get_unique_id_from_jwt_payload", return_value=jwt_response)
@patch.object(Jwt, "get_experience_time_from_jwt_payload", return_value=jwt_response)
@patch.object(UpdateMarketTimeExperience, "update_market_time_experience", return_value=Exception)
async def test_when_sending_wrong_params_to_update_market_experience_time_then_return_the_expected_error(
        mock_update_market_time_experience,
        mock_get_experience_time_from_jwt_payload,
        mock_get_unique_id_from_jwt_payload,
        mock_experience_time_enum_validation,
        mock_decode_payload
):
    app = Flask(__name__)
    with app.test_request_context(
            json=None,
            headers=Headers({"x-thebes-answer": "jwt_to_decode_stub"}),
    ).request as request:
        with pytest.raises(Exception):
            await update_experience_time(
                request_body=None
            )
