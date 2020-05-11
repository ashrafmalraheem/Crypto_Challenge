from Crypto.Cipher import AES
from base64 import b64decode
'''Read the file as byte coded'''
with open('7.txt','r') as input:
    text = input.read()
decoded = b64decode(text)
key = b'YELLOW SUBMARINE'
ciphering = AES.new(key,AES.MODE_ECB)
decrypted = ciphering.decrypt(decoded)
print(str(decrypted,'utf-8'))
