# STANDARD IMPORTS
from pydantic import BaseModel

# PROJECT IMPORTS
from src.domain.models.jwt.models import Jwt


class TimeExperienceRequest(BaseModel):
    time_experience: str


class TimeExperienceTemplates:

    @classmethod
    def user_time_experience_schema_template(
            cls, time_experience: TimeExperienceRequest, jwt_data: Jwt
    ) -> dict:
        time_experience_template = {
            "unique_id": jwt_data.get_unique_id_from_jwt_payload(),
            "time_experience": time_experience
        }
        return time_experience_template
