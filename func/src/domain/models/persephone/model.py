class Templates:

    @classmethod
    def get_user_time_experience_schema_template_with_data(
            cls, time_experience: str, unique_id: str
    ) -> dict:
        return {
            "unique_id": unique_id,
            "time_experience": time_experience,
        }
