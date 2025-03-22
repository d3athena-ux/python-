from whois import whois 
from scapy.all import *
from random import randint
def main():
    ans,uans=sr(IP(dst="[Ä¿±êµÄIP]")/TCP(dport=80,flags="S"))
    for snd,rcv in ans:
        pirnt(rcv,sprintf("%IP,src% is up"))
    pass
if __name__== '__main__':
    main()