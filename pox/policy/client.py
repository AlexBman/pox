from pox.core import core

__author__ = 'berryman'

def create_request(event):

def packet_handler (event):
    # Note the two MACs
    create_request(event)

def launch():
    core.openflow.addListenerByName("PacketIn",packet_handler,priority=1)
