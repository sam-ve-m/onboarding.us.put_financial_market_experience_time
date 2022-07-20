# STANDARD IMPORTS
from http import HTTPStatus
from flask import request, Response, Request, Flask

# THIRD PART IMPORTS
from etria_logger import Gladsheim

# PROJECT IMPORTS
from src.domain.enums.status_code.enum import InternalCode
from src.domain.models.time_experience.model import TimeExperienceModel
from src.domain.response.model import ResponseModel
from src.services.jwt_service.service import JWTService
from src.services.update_time_experience.service import UpdateMarketTimeExperience
from src.domain.exceptions.exceptions import (
    InvalidUsOnboardingStep,
    InvalidBrOnboardingStep,
    ErrorOnDecodeJwt,
    NotSentToPersephone,
    UniqueIdWasNotUpdate,
    InvalidParams, ErrorOnGettingDataFromStepsBr, ErrorOnGettingDataFromStepsUs)

app = Flask(__name__)


@app.route('/put/update_market_experience_time')
async def update_market_experience_time(
        request_body: Request = request) -> Response:
    thebes_answer = request_body.headers.get("x-thebes-answer")

    try:
        jwt_data = await JWTService.decode_jwt_from_request(jwt_data=thebes_answer)
        time_experience = TimeExperienceModel(**request_body.json).dict()
        payload = {"x-thebes-answer": jwt_data}
        payload.update(time_experience)
        service_response = await UpdateMarketTimeExperience.update_market_time_experience(
            thebes_answer=thebes_answer, jwt_data=payload
        )

        response = ResponseModel(
            success=True,
            code=InternalCode.SUCCESS,
            message="The Time Experience of Financial Market Was Updated Successfully",
            result=service_response
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except InvalidBrOnboardingStep as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.INVALID_BR_ONBOARDING_STEP,
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

    except InvalidUsOnboardingStep as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.INVALID_US_ONBOARDING_STEP,
            message="Invalid Onboarding Step"
        ).build_http_response(status=HTTPStatus.UNAUTHORIZED)
        return response

    except InvalidParams as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.INVALID_PARAMS,
            message="Invalid Params Were Sent"
        ).build_http_response(status=HTTPStatus.UNAUTHORIZED)
        return response

    except ErrorOnGettingDataFromStepsBr as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.ERROR_ON_GETTING_DATA_FROM_BR_STEPS,
            message="Http Error while getting data from fission"
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

    except ErrorOnGettingDataFromStepsUs as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            result=False,
            success=False,
            code=InternalCode.ERROR_ON_GETTING_DATA_FROM_US_STEPS,
            message="Http Error while getting data from fission"
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
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

if __name__ == "__main__":
    app.run(debug=True)
