from pox.core import core
from pox.lib.revent import EventHalt
from pox.lib.addresses import EthAddr
import requests


def create_request(event, api_auth=('dmz_admin', 'dmz_admin')):
    payload = {'mac_address': [EthAddr(event.parsed.src).toStr(''), EthAddr(event.parsed.src).toStr('')]}
    flow = requests.get('http://localhost:8000/flow/', params=payload, auth=api_auth)
    if flow.status_code != 200:
        return EventHalt
    else:
        return flow.json()


def packet_handler(event):
    create_request(event)


def launch():
    core.openflow.addListenerByName("PacketIn", packet_handler, priority=1)
