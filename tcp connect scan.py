#��Ŀ�귢��syn����������syn+ack,�յ�֮�󷵻ظ�����ack���ɹ�����tcp����
from whois import whois 
from scapy.all import *
from random import randint
def main():
    ip="[Ŀ���IP]��
    port=80
    packet=IP(dst=ip)/TCP(sport=12345,dport=port,flags="S")
    resp=sr1(packet,timeout=20)
    if(str(type(resp))=="<type 'NoneType'>"):
        print("port %s is closed"%(port))
    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags==0x12):
            send_rst =sr(IP(dst=ip)/TCP(sport=12345,dport=port,flags="AR"),timeout=20)
            print("port %s is open"%(port))
        elif(resp.getlayer(TCP).flags==0x14):
            print("port %s is down"%(port))
    pass
if __name__== '__main__':
    main()