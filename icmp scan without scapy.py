from whois import whois 
from scapy.all import *
from random import randint
def main():
    ip_id=randint(1,65535)
    icmp_id=randint(1,65535)
    icmp_seq=randint(1,65535)
    packet=IP(dst="[Ŀ���IP]",ttl=64,id=ip_id)/ICMP(id=icmp_id,seq=icmp_seq)/b'rootkit'
    result=sr1(packet,timeout=1,verbose=False)
    if result:
        for rcv in result:
            scan_ip=rcv[IP].src
            print(scan_ip+' is alive')
    else:
        print(" is down")
if __name__== '__main__':
    main()