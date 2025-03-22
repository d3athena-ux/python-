from whois import whois 
from scapy.all import *
from random import randint
def main():
    ip="[Ä¿±êµÄIP]"
    dport=randint(1,65535)
    packet=IP(dst=ip)/TCP(flags="A",dport=dport)
    response=sr1(packet,timeout=1.0,verbose=0)
    if response:
        #RST
        if int(response[TCP].flags)==4:
            time.sleep(0.5)
            print(ip+' is up')
        else:
            print(ip+' is down')
    pass
    
if __name__== '__main__':
    main()