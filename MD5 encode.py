from hashlib import md5
def md5hs(str1):
    s=str1
    new_md5=md5()
    new_md5.update(s.encode(encoding="utf-8"))
    return new_md5.hexdigest()
def main():
    a=input("ÇëÊäÈëÎÄ±¾")
    b=md5hs(a)
    print(b)
    pass
if __name=='__main__':
    main()