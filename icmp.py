from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr1

try:
        
        src_ip = input("source ip > ")
        dst_ip = input("destination > ")

        ip_head = IP(src=src_ip , dst=dst_ip)

        icmp_option = ICMP(id=1000)

        full_packets = ip_head / icmp_option

        print(full_packets)

        sender_packet = sr1(full_packets)

        if sender_packets:
            print(sender_packets)

        print(ip_head )
except Exception:
        print("error")
        
