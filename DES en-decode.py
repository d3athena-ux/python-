from Cryptodome.Cipher import DES
import binascii
def main():
    key=b'12345678'
    des=DES.new(key.DES.MODE_ECB)
    text="haha123 nihao"
    text=text+(8-(len(text)%8))*"="
    encrypt_text=des.encrypt(text.encode())
    encrypt_res=binascii.b2a_hex(encrypt_text)
    print(encrypt_res)
    #º”√‹
    encrypto_res=encrypt_res
    encryt_text=binascii.a2b._hex(encrypto_res)
    decrypt_res=des.decrypt(encryt_text)
    print(decrypt_res)
    #Ω‚√‹
    pass
if __name__=='__main__':
    main()