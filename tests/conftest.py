import pytest
from keysfood.app import create_app


@pytest.fixture(scope="module")
def app():
    """Instance of Main flaks app"""
    return create_app()

