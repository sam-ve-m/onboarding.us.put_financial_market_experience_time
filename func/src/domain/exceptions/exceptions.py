class ErrorOnDecodeJwt(Exception):
    msg = "Jormungandr-Onboarding::decode_jwt_and_get_unique_id::Fail when trying to get unique_id," \
          " jwt not decoded successfully"


class InvalidBrOnboardingStep(Exception):
    msg = "ValidateOnboardingStepsBR.onboarding_br_step_validator::you're not in this step"


class InvalidUsOnboardingStep(Exception):
    msg = "ValidateOnboardingStepsUS.onboarding_us_step_validator::you're not in this step"


class DriveWealthConnectionError(Exception):
    msg = "DWTransport::call_registry_user_patch::Not able to get the response from Drive Wealth"


class NotSentToPersephone(Exception):
    msg = "UpdateMarketTimeExperience.update_market_time_experience::sent_to_persephone:: the data was not sent to persephone"


class ClientDataWasNotUpdatedDriveWealth(Exception):
    msg = "DriveWealthService.registry_update_client::was_updated::Data Was Not Updated"


class UniqueIdWasNotUpdate(Exception):
    msg = "UpdateMarketTimeExperience.update_market_time_experience::was_updated:: The user was not updated"


class InvalidParams(Exception):
    msg = "Jormungandr-Onboarding::w8_confirmation_param::Invalid params were sent"


class UserUniqueIdDoesNotExists(Exception):
    pass


class W8DocumentWasNotUpdated(Exception):
    pass


class WasNotSentToPersephone(Exception):
    msg = "common.process_issue::W8DocumentService::update_w8_form_confirmation::sent_to_persephone:false"


class InternalServerError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class ForbiddenError(Exception):
    pass


class BadRequestError(Exception):
    pass
