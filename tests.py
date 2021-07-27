import pytest

import app as tested_app


@pytest.fixture
def client():
    tested_app.app.config['TESTING'] = True
    app = tested_app.app.test_client()
    return app


def test_get_one(client):
    r = client.get('/api/v1/1')
    # assert r.data.decode('utf-8').startswith('У меня получилось!')
    assert r.status_code == 200


def test_get_all(client):
    r = client.get('/api/v1')
    # assert r.data.decode('utf-8').startswith('У меня получилось!')
    assert r.status_code == 200


def test_post(client):
    r = client.post('/')
    assert r.status_code == 404
