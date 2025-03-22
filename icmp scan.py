from whois import whois
def main():
    data=whois("www.baidu.com")
    print(data)
    ip=socket.gethostbyname("www.baidu.com")
    print(ip)
    pass
if __name__== '__main__':
    main()