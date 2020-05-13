from base64 import b64decode
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
def PKCS(text:bytes,blocksize):
    for i in range(blocksize-(len(text))%blocksize):
        text += b'\x00'
    return  text

def encryption_oracle(plain_text):
    ''' Generate random keys and random IV'''
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    '''Add a random number of random bytes before and after the plain text'''
    append_length = [5,6,7,8,9,10]
    random_length = append_length[(get_random_bytes(1)[0])%6]
    before_plain_text = get_random_bytes(random_length) + plain_text
    random_length = append_length[(get_random_bytes(1)[0])%6]
    plain_text = before_plain_text + get_random_bytes(random_length)
    plain_text = PKCS(plain_text,16)
    ''' Encrypt using Two modes EBC or CBC, the mode is choosen randomly'''
    ''' EBC 0
        CBC 1
    '''
    AES_MODE = (get_random_bytes(1)[0])%2
    if AES_MODE == 0: # EBC Mode
        print('AES_EBC mode')
        ciphering = AES.new(key, AES.MODE_ECB)
        cipher_text = ciphering.encrypt(plain_text)
        return cipher_text
    print('AES_CBC mode')
    ciphering = AES.new(key, AES.MODE_CBC,iv=iv)
    cipher_text = ciphering.encrypt(plain_text)
    return cipher_text


text = b'My name is oracle'

print(encryption_oracle(text))

