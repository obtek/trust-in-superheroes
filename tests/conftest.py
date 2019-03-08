import pytest
from flask import Response
from flask import Flask

from api import create_app

@pytest.fixture
def app():
    app = create_app()

    return app