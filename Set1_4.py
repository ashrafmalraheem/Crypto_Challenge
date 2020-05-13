# Crypto challenge Set 1 Challenge 4
print("Crypto challenge Set 1 Challenge 4")
from collections import Counter

def obtain_cipher_text(cipher_text):
    ''' To obtain the ciphered text: the function will count the number of
        frequently used letters/bytes. The line with maximum number of
        frequently used letters is the ciphered one.
    '''
    length_of_letter_frequency = 1000 # some initial value
    line_index = 0
    for i in range(len(cipher_text)):
        if length_of_letter_frequency > len(Counter(cipher_text[i]).most_common()):
            length_of_letter_frequency = len(Counter(cipher_text[i]).most_common())
            line_index = i
    return cipher_text[line_index]

def decrypt(ciphter_text:bytes,key:bytes):
    decrypted =b''
    for i in range(len(ciphter_text)):
         decrypted += (key[i%len(key)] ^ ciphter_text[i]).to_bytes(1,'big')
    return decrypted

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



cipher_bytes = []
with open('4.txt', 'r') as input_file:
    while True:
        cipher_text = input_file.readline().rstrip('\n')
        if cipher_text == '':
            break
        cipher_bytes.append(int(cipher_text,16).to_bytes(int(len(cipher_text)/2),'big'))


obtained_text = [b'']
obtained_text[0] = obtain_cipher_text(cipher_bytes) # work with it as bytearray place the cipher text in first location
print('The key: ',find_key(obtained_text).hex())
print('Decrypted Text: ',str(decrypt(obtained_text[0],find_key(obtained_text)),'utf-8'))
