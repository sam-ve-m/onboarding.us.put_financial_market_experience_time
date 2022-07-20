# STANDARD IMPORTS
from unittest.mock import patch
import pytest
from flask import Flask
from werkzeug.datastructures import Headers

# PROJECT IMPORTS
from func.main import update_experience_time

# STUB IMPORTS
from src.services.jwt_service.service import JWTService
from src.services.update_time_experience.service import UpdateMarketTimeExperience
from tests.main_stub import request_body_stub, decoded_jwt_stub


@pytest.mark.asyncio
@patch.object(JWTService, "decode_jwt_from_request", return_value=decoded_jwt_stub)
@patch.object(UpdateMarketTimeExperience, "update_market_time_experience", return_value=True)
async def test_when_sending_right_params_to_update_market_experience_time_then_return_the_expected(
        mock_decode_jwt_from_request,
        mock_update_market_time_experience
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


@pytest.mark.asyncio
@patch.object(JWTService, "decode_jwt_from_request", return_value=Exception)
@patch.object(UpdateMarketTimeExperience, "update_market_time_experience", return_value=Exception)
async def test_when_sending_right_params_to_update_market_experience_time_then_return_the_expected(
        mock_decode_jwt_from_request,
        mock_update_market_time_experience
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
