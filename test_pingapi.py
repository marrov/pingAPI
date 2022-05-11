from fastapi.testclient import TestClient

from pingapi import app

client = TestClient(app)

ok_ping = {
    'host_addr': 'www.kambi.com',
    'n_pings': 5,
    'interval': 0.2
}

bad_website = {
    'host_addr': 'www.qwerasdfzxcv.com',
    'n_pings': 5,
    'interval': 0.2
}

flood = {
    'host_addr': 'www.kambi.com',
    'n_pings': 5,
    'interval': 0.01
}

def test_ok_ping():
    response = client.post( '/ping/', json=ok_ping)
    assert response.status_code == 200
    assert response.json()['destination'] == ok_ping['host_addr']
    assert response.json()['packet_transmit'] == ok_ping['n_pings']


def test_bad_website():
    response = client.post('/ping/', json=bad_website)
    assert response.status_code == 400


def test_flood():
    response = client.post('/ping/', json=flood)
    assert response.status_code == 400
