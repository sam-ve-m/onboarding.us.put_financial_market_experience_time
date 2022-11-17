# STANDARD IMPORTS
from pydantic import BaseModel


class TimeExperienceRequest(BaseModel):
    time_experience: str


class TimeExperienceTemplates:
    @classmethod
    def user_time_experience_schema_template(
        cls, time_experience: str, unique_id: str
    ) -> dict:
        time_experience_template = {
            "unique_id": unique_id,
            "time_experience": time_experience,
        }
        return time_experience_template
