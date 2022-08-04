# STANDARD IMPORTS
from http import HTTPStatus
from flask import request, Response, Request

# THIRD PART IMPORTS
from etria_logger import Gladsheim

# PROJECT IMPORTS
from src.domain.enums.status_code.enum import InternalCode
from src.domain.models.jwt.models import Jwt
from src.domain.models.time_experience.model import TimeExperienceRequest
from src.domain.models.response.model import ResponseModel
from src.services.update_time_experience.service import UpdateMarketTimeExperience
from src.domain.exceptions.exceptions import (
    ErrorOnDecodeJwt,
    NotSentToPersephone,
    UniqueIdWasNotUpdate,
    InvalidOnboardingStep,
    TransportOnboardingError
)


async def update_experience_time(request_body: Request = request) -> Response:
    thebes_answer = request_body.headers.get("x-thebes-answer")

    try:
        jwt_data = Jwt(jwt=thebes_answer)
        await jwt_data()

        time_experience_request = TimeExperienceRequest(**request_body.json)

        service_response = await UpdateMarketTimeExperience.update_market_time_experience(
            jwt_data=jwt_data,
            time_experience_request=time_experience_request
        )

        response = ResponseModel(
            success=True,
            code=InternalCode.SUCCESS,
            message="The Time Experience of Financial Market Was Updated Successfully",
            result=service_response
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except InvalidOnboardingStep as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.INVALID_ONBOARDING_STEP,
            message="Invalid Onboarding Step"
        ).build_http_response(status=HTTPStatus.UNAUTHORIZED)
        return response

    except ErrorOnDecodeJwt as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.JWT_INVALID,
            message="Error On Decoding JWT"
        ).build_http_response(status=HTTPStatus.UNAUTHORIZED)
        return response

    except TransportOnboardingError as error:
        Gladsheim.error(error=error, message=error.msg)
        response = ResponseModel(
            success=False,
            code=InternalCode.TRANSPORT_ON_BOARDING_ERROR,
            message="update_w8_form_confirmation::sent_to_persephone:false"
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

    except NotSentToPersephone as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.NOT_SENT_TO_PERSEPHONE,
            message="Not Sent to Persephone"
        ).build_http_response(status=HTTPStatus.UNAUTHORIZED)
        return response

    except UniqueIdWasNotUpdate as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.UNIQUE_ID_WAS_NOT_UPDATED,
            message="Unique Id Was Not Updated"
        ).build_http_response(status=HTTPStatus.UNAUTHORIZED)
        return response

    except Exception as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.INTERNAL_SERVER_ERROR,
            message="Unexpected error occurred"
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response
