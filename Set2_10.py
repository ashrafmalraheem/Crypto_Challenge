from Crypto.Cipher import AES
from base64 import b64decode
def PKCS(text:bytes,blocksize):
    for i in range(blocksize-len(text)):
        text += b'\x00'
    return  text

'''Read the file as byte coded'''
with open('10.txt','r') as input:
    text = input.read()
decoded = b64decode(text)
key = b'YELLOW SUBMARINE'
IV = b''
IV = PKCS(IV,16)
ciphering = AES.new(key,AES.MODE_CBC,iv=IV)
decrypted = ciphering.decrypt(decoded)
print(str(decrypted,'utf-8'))
