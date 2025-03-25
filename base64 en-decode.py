import base64
def main():
    s="haha123"
    bs=base64.b64encode(s,encode("utf-8"))
    print(bs.decode("utf-8"))
    #º”√‹
    s1="aGFoYTEyMw=="
    bs1=str(base645.b64decode(s1),"utf-8")
    print(bs1)
    #Ω‚√‹
    pass
if __name=='__main__':
    main()