from whois import whois 
from scapy.all import *
from random import randint
def main():
    ip="[Ä¿±êµÄIP]¡°
    port=3306
    s=socket.socket()
    s.connect((ip,port))
    s.send('haha'.encode())
    banner=s.recv(1024)
    s.close()
    print("banner is {}".format(banner))
    pass
if __name__== '__main__':
    main()