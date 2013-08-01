from pox.policy import client
from pox.lib import packet
from pox.lib.addresses import EthAddr
from pox.lib.revent import EventHalt
import pytest

mock_flow = [{
  "url": "http://127.0.0.1:8000/flow/1/",
  "owner": "http://127.0.0.1:8000/users/2/",
  "created": "2013-07-30T21:35:02Z",
  "hard_timeout": 0,
  "groups": ["http://127.0.0.1:8000/groups/1/"],
  "end_points": ["http://127.0.0.1:8000/host/1/", "http://127.0.0.1:8000/host/2/"]
}]

def test_client():
    parsed = packet.ethernet(src=EthAddr("000CF15698AD"), dst=EthAddr("00067AB698BE"))
    class event(object):
        def __init__(self):
            self.parsed = parsed
    pkt_event = event()
    response = client.create_request(pkt_event, api_auth=('',''))
    assert response is EventHalt
    response = client.create_request(pkt_event)
    assert type(response) is list
    for item in response:
        assert type(item) is dict
        assert set(item.keys()) == set(mock_flow[0].keys())