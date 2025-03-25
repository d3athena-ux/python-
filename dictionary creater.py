import sys,random
import time
import itertools
def main():
    words="1234567890abcdefghijklmnopqrstuvwxyz"
    temp=itertools.permutations(words,6)
    passwords=open("dic.txt","a")
    for i in temp:
        passwords.write("",join(i))
        passwords.write("",join("\n"))
    passwords.close()
    pass
if __name__=='__main__':
    main()