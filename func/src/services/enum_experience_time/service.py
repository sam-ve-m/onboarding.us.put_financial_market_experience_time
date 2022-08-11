# PROJECT IMPORTS
from etria_logger import Gladsheim

from src.domain.exceptions.exceptions import EnumSentIsNotaValidEnum
from src.domain.models.time_experience.model import TimeExperienceRequest
from src.domain.validators.experience_time_enum.validator import ValidateEnumFromRequest
from src.repositories.experience_time_enum.repository import ExperienceTimeEnumRepository


class ExperienceTimeEnumService:

    @classmethod
    def experience_time_enum_validation(cls, time_experience_model: TimeExperienceRequest) -> bool:

        enums_data = ExperienceTimeEnumRepository.get_experience_time_enum()
        response = dict(enums_data)

        try:
            is_valid = ValidateEnumFromRequest.check_validity_experience_time_enum(
                enums_dict=response,
                time_experience_model=time_experience_model.time_experience
            )

            return is_valid
        except Exception as err:
            Gladsheim.error(
                message=f"Error: {err} ::SendToIara::register_user_time_experience_log_on_persephone::"
                        f"Error on trying to register log")
            raise EnumSentIsNotaValidEnum

