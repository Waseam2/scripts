from scapy.all import Ether , ARP , srp

ether_head = Ether(dst="ff:ff:ff:ff:ff:ff")


ip_range = input("enter ip > ")

arp_head = ARP(pdst=ip_range)

packet , nodata = srp((ip_range / arp_head), timeout=2 )

print(packet.show())
for send , recive in packet:
    print(recive[Ether].psrc)

