from scapy.all import *


def packet_show(packet):
    print(packet.show())


sniff(packet_show, 10)
