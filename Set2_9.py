
def PKCS(text:bytes,blocksize,pad=b'\x00'):
    if len(text)%blocksize == 0:
        return text
    text += pad
    return PKCS(text,blocksize,pad)


test = b'YELLOW SUBMARINE'
print(PKCS(test,20,b'\x04'))