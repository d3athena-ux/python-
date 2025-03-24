from scapy.all import *
import whois
import time
def main():
    while 1:
        packet = Ether(src=RandMAC(), dst=RandMAC()) / IP(src=RandIP(), dst=RandIP()) / ICMP()
        time.sleep(0.5)
        sendp(packet)
        print(packet.summary())
    pass
if __name__ == '__main__':
    main()