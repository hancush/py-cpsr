import pytest

from py_cpsr.scrape import ICPSR

from config import ICPSR_USERNAME, ICPSR_PASSWORD


@pytest.fixture
def session():
    return ICPSR(ICPSR_USERNAME, ICPSR_PASSWORD)
