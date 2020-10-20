import os
import pytest


@pytest.fixture(scope="session")
def env_setup():
    db_path = os.environ["SQLITE_DB"]
    yield db_path

