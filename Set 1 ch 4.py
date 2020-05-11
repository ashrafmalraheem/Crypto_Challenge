# Crypto challenge Set 1 Challenge 4
print("Crypto challenge Set 1 Challenge 4")
from collections import Counter
def Fixed_XOR(param1,param2):
    return param1 ^ param2
str_key = '0x'
key = '35'  # the key was found to be the 35 after searching for space the most frequent used letter

for i in range(30):
    str_key += key
    

the_key = int(str_key,16)
print(hex(the_key))
line_number = 1
with open('Text.txt', 'rb') as input_file:
    with open('Results.txt','w') as output_file:
        with open('Stats.txt','w') as stat_file:
            while True:
                text = (input_file.readline()).rstrip(b'\n')
                if text == b'':
                    break
                str_text = int(str(text, 'utf-8'), 16)  # convert the data from byte to string then to integer
                length = int((len(str(hex(str_text)))) / 2)  # Get the length of the data, note it is two bytes
                byte_inputs = str_text.to_bytes(length, 'big')
                # print("Decrypted Text =", byte_inputs)
                print(line_number, "", str(Counter(byte_inputs)), file=stat_file)
                # print(line_number,"  ",hex(str_text))
                xor = the_key ^ str_text
                output = xor.to_bytes(length, 'big')
                print(line_number, ' ', length, ' ', output, file=output_file)
                print(line_number, ' ', length, ' ', output)
                line_number += 1


