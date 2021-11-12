import pytest

import server


@pytest.fixture()
def client():
    server_test = server
    app = server_test.app
    with app.test_client() as client:
        yield client
