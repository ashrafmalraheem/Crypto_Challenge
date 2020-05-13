
def PKCS(text:bytes,blocksize):
    for i in range(blocksize-(len(text))%blocksize):
        text += b'\x00'
    return  text


test = b'YELLOW SUBMARINE'
print(PKCS(test,20))