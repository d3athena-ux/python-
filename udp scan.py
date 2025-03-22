from whois import whois 
from scapy.all import *
from random import randint
def main():
    ip="[Ä¿±êµÄIP]"
    ans,uans=sr(IP(dst=ip)/UDP(dport=80))
    for snd,rcv in ans:
        print(rcv.sprintf("%IP.src% is up"))
    pass
if __name__== '__main__':
    main()