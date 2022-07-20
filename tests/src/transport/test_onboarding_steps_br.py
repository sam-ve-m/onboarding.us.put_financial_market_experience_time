# STANDARD IMPORTS
from unittest.mock import patch, AsyncMock
import pytest

# PROJECT IMPORTS
from func.src.transport.onboarding_steps_us import ValidateOnboardingStepsUS
from tests.src.transport.stub_onboarding_steps import us_steps_result_stub


@pytest.mark.asyncio
@patch.object(
    ValidateOnboardingStepsUS,
    "_ValidateOnboardingStepsUS__get_onboarding_steps_us",
    return_value=us_steps_result_stub)

