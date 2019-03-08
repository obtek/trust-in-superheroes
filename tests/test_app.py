import pytest

def test_get_index(client):
    rv = client.get('/heroes')
    assert rv.status_code == 200