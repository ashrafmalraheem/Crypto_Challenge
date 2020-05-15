from base64 import b64decode
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

def PKCS(text: bytes, blocksize, pad=b'\x00'):
    if len(text) % blocksize == 0:
        return text
    text += pad
    return PKCS(text, blocksize, pad)


def encryption_oracle(plain_text):
    ''' Generate random keys and random IV'''
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    '''Add a random number of random bytes before and after the plain text'''
    append_length = [5, 6, 7, 8, 9, 10]
    random_length = append_length[(get_random_bytes(1)[0]) % 6]
    before_plain_text = get_random_bytes(random_length) + plain_text
    random_length = append_length[(get_random_bytes(1)[0]) % 6]
    plain_text = before_plain_text + get_random_bytes(random_length)
    plain_text = PKCS(plain_text, 16)
    ''' Encrypt using Two modes EBC or CBC, the mode is choosen randomly'''
    ''' EBC 0
        CBC 1
    '''
    AES_MODE = (get_random_bytes(1)[0]) % 2
    if AES_MODE == 0:  # EBC Mode
        print('AES_EBC mode')
        ciphering = AES.new(key, AES.MODE_ECB)
        cipher_text = ciphering.encrypt(plain_text)
        return cipher_text
    print('AES_CBC mode')
    ciphering = AES.new(key, AES.MODE_CBC, iv=iv)
    cipher_text = ciphering.encrypt(plain_text)
    return cipher_text


def AES_128_ECB(plain_text, random_key):
    ''' Encrypt using AES-ECB with random key and append some unknown string to the key '''
    unknown_string = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg' \
                     'aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq' \
                     'dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg' \
                     'YnkK'
    plain_text += b64decode(unknown_string)
    plain_text = PKCS(plain_text, 16)
    ''' Encrypt using Two modes EBC'''
    # print('AES_EBC mode')
    ciphering = AES.new(random_key, AES.MODE_ECB)
    cipher_text = ciphering.encrypt(plain_text)
    return cipher_text


def get_blocksize(func):
    ''' You can determine the block size by getting the cipher text
        from encrypt function by passing 1 additional byte each time
        and monitor the length of the cipher text. when it increments
        the increment is the block size
    '''
    ''' future work it should take the function name as a parameter
     to test many functions not only the AES_128
     '''
    test_text = b'A'
    key = get_random_bytes(16)
    initial_length = len(AES_128_ECB(test_text, key))
    final_length = initial_length
    while True:
        if final_length != initial_length:
            return final_length - initial_length
        test_text += b'A'
        final_length = len(AES_128_ECB(test_text, key))


def get_unknowstringsize(func):
    ''' To determine the unknown string appended to plain text
        by the encrypt function. Increment the size of the test
        text by one. When the size of cipher text increment by
        1 block size return the difference between the inital
        length and the counter
        '''
    ''' future work it should take the function name as a parameter
     to test many functions not only the AES_128
     '''
    key = get_random_bytes(16)
    test_text = b'A'
    initial_length = len(AES_128_ECB(test_text, key))
    final_length = initial_length
    i = 1
    while True:
        if final_length != initial_length:
            return initial_length - i + 1
        test_text += b'A'
        i += 1
        final_length = len(AES_128_ECB(test_text, key))


def is_AES_ECB_mode(func):
    ''' This function will test against the AES ECB mode
        if it find match it will return true
    '''
    key = get_random_bytes(16)
    blocksize = get_blocksize(AES_128_ECB(b' ', key))
    blocksize_minus1 = PKCS(b'A', blocksize * 2, b'A')
    cipher_text = AES_128_ECB(blocksize_minus1, key)
    if find_match(cipher_text, blocksize)[0]:
        print("AES-ECB is used")
        return True
    return False


def find_match(cipher, KeyLength=16):
    found = False
    ''' if it is a single row bytes'''
    if str(type(cipher[0])) == '<class \'int\'>':
        cipher_array = [b'']
        cipher_array[0] = cipher
        cipher = cipher_array
    for k in range(int(len(cipher))):
        for l in range(int(len(cipher[0]) / KeyLength)):
            block1 = cipher[k][(l) * KeyLength:(l + 1) * KeyLength]
            # print(len(block1),block1)
            count_match = 0
            # match_location = [(,)]
            for i in range(int(len(cipher))):
                for j in range(int(len(cipher[i]) / KeyLength)):
                    # if hamming_distance(block1,cipher_text[i][j*keylength:(j+1)*keylength]) == 0:
                    if block1 == cipher[i][j * KeyLength:(j + 1) * KeyLength]:
                        if j != l:
                            # print("Find Match! in line",i,'Block',j)
                            count_match += 1
                            found = True
    return found, count_match

key = get_random_bytes(16)
random_text = b'adsf'
blocksize = get_blocksize(AES_128_ECB(random_text, key))
attack_result = b''
extend = int(get_unknowstringsize(AES_128_ECB(random_text,key))/blocksize)+1
found_byte = b''
print(is_AES_ECB_mode(AES_128_ECB(random_text,key)))
if is_AES_ECB_mode(AES_128_ECB(random_text,key)):
    print('AES_ECB Brute force attack will be implemented')
else:
    exit()
for j in range(1,get_unknowstringsize(AES_128_ECB(random_text,key))):
    for i in range(256):
        test_block = PKCS(b'A',extend*blocksize-j,b'A')
        test_cipher = AES_128_ECB(test_block,key)
        cipher = AES_128_ECB(test_block+found_byte+i.to_bytes(1,'big'),key)
        print(found_byte+i.to_bytes(1,'big'))
        working_block = int(get_unknowstringsize(AES_128_ECB(random_text,key))/blocksize)
        if test_cipher[(working_block)*blocksize:(working_block+1)*blocksize] == cipher[(working_block)*blocksize:(working_block+1)*blocksize]:
            found_byte += i.to_bytes(1,'big')
            break
print('The found unknown string by brute force attack is:')
print(found_byte.decode('utf-8'))
exit()
