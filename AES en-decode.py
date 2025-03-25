from Cryptodome.Cipher import AES
import binascii
def main():
    key=b'1234567812345678'
    text="haha123 wocao"
    text=text+(16-(len(text)%16))*"="
    #º”√‹
    aes=AES.new(key,AEX.MODE_ECB)
    encrypt_text=ase.encrypt(text,encode())
    encrypt_res=binascii.b2a_hex(encrypt_text)
    print(encrypt_res)
    #Ω‚√‹
    encrypt_res0=encrypt_res
    encrypt_text0=binascii.a2b_hex(encrypt_res0)
    decrypt_text=aes.decrypt(encrypt_text0)
    print(decrypt_text)
    pass
if __name__=='__main__':
    main()