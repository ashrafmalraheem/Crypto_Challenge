from base64 import b64decode
from collections import Counter


def hamming_distance(block1:bytes,block2:bytes):
    '''The hamming distance function in implemented with counting the One's
        after making XOR between two blocks  '''
    '''Convert the two blocks into hexadecimal numbers'''
    b1_hex = int(block1.hex(),16)
    b2_hex = int(block2.hex(),16)
    ''' Make xoring between the two decimal numbers '''
    XOR = b1_hex ^ b2_hex
    ''' Count the number of One's resulted from the XOR by convert the result 
    to binary and strip the Zero's and the b letter for Binary'''
    distance = len(bin(XOR).replace('0','')) - 1
    return  distance

def find_keylength(byte_text:bytes,mini_keylength=2,max_keylegnth=50,mini_block_size=1,max_block_size=30):
    saved_keylength = []
    '''The highest loop to calculated normalized hamming/distance function with different block sizes'''
    for no_of_blocks in range(mini_block_size,max_block_size):
        initial_normalized_distance = 3
        '''Seconday loop to calculate the normalized hamming/distance function for the given block size '''
        for keylength in range(max_keylegnth,mini_keylength,-1):
            normalized = 0
            k = 0
            for j in range(no_of_blocks):
                normalized += hamming_distance(decoded[k * keylength:(k + 1) * keylength], decoded[(k + 1) * keylength: (k + 2) * keylength])
                k += 2
                '''Take the average and normalize to keylength'''
            normalized = normalized/(no_of_blocks*keylength)
            ''' If the normalized value is less than the initial one, take the minimum and assign it as the initial'''
            if normalized < initial_normalized_distance:
                initial_normalized_distance = normalized
                saved_keylength.append(keylength) # save all keylengths with minimal normalized distance values
    ''' To return the keylength with maximum number of occurrence in the normalized list'''
    from collections import Counter
    print("Found Keylength = ",Counter(saved_keylength).most_common(1)[0][0])
    return Counter(saved_keylength).most_common(1)[0][0]

def transpose(byte_text:bytes,keylength):
    ''' Transpose data into set of data with keylength'''
    transposed_bytes = [b'']*keylength
    for i in range(len(byte_text)):
        transposed_bytes[i%keylength] += byte_text[i].to_bytes(1,'big')
    return transposed_bytes

def find_key(cipher_text:list):
    ''' To find key using brute force attack
    The most common letters are used in dictionary, including space
    The most common letter in cipher text is XORed with the brute force
    dictionary letters. The obtained key will be tested against full cipher
    text. it is all alphabetical letters the key is found.
    '''
    brute_force_dict = b' etario'
    my_dictionary = b' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890(),.\'\"\n:-'
    the_key = b''
    save_key = b''
    ''' Start raw by raw of transposed data'''
    for k in range(len(cipher_text)):
        '''Obtain the most common letter in the Kth raw/set of data'''
        most_common_ciphered_letter = Counter(cipher_text[k]).most_common(1)[0][0]
        minimal_decrypted_data_length = len(cipher_text[k])
        '''Xor with the most common letter with the brute force dictionary '''
        for i in range(len(brute_force_dict)):
            key = brute_force_dict[i] ^ most_common_ciphered_letter
            decrypted_bytes = b''
            ''' Now decrypt the cipher text with the current obtained key'''
            for j in range(len(cipher_text)):
                decrypted_bytes += (key ^ cipher_text[k][j]).to_bytes(1,'big')
            ''' Strip my dictionary letters from the decrypted data, the correct key will 
                give the minimal length of data
            '''
            if minimal_decrypted_data_length > len(decrypted_bytes.strip(my_dictionary)):
                minimal_decrypted_data_length = len(decrypted_bytes.strip(my_dictionary))
                save_key = key    # the correct key with maximum valid ascii letters
        the_key += save_key.to_bytes(1,'big')
    return the_key

def decrypt(ciphter_text:bytes,key:bytes):
    decrypted =b''
    for i in range(len(ciphter_text)):
         decrypted += (key[i%len(key)] ^ ciphter_text[i]).to_bytes(1,'big')
    return decrypted

'''Read the file as byte coded'''
with open('6.txt','r') as input:
    text = input.read()

decoded = b64decode(text)
#find_keylength(decoded)

transposed = transpose(decoded,find_keylength(decoded))

#print('the key = ',(find_key(transposed)))

#print(str(decrypt(decoded,find_key(transposed)),'utf-8'))
