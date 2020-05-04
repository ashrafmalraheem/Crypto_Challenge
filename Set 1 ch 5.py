# Crypto challenge Set 1 Challenge 4
print("Crypto challenge Set 1 Challenge 4")
from collections import Counter
def Fixed_XOR(param1,param2):
    return param1 ^ param2
MyText =  'Bur'
MyText_bytes = MyText.encode().rstrip()
key = 'ICE'  # the key is ICE
key_size = 3
key_bytes = key.encode()
line_number = 1
result = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
def key_stretch(my_key,length):
    str_key = ''
    i = 0
    for i in range(length + 1):
        str_key += my_key

    return str_key.encode()

def dkey_stretch(str_key,length):
    my_key = str_key.encode()
    temp_key = ''
    return_key = ''
    for i in range(len(str_key)):
        in_hex = hex(my_key[i])
        temp_key += str(in_hex)[2:].zfill(2)
    print(temp_key,"size of temp key",len(temp_key))
    for i in range(length):
        return_key +=temp_key[i%len(temp_key)]
    return return_key

with open('Text Ch5.txt', 'rb') as input_file:
    with open('Encrypted.txt','w') as output_file:
        with open('Encrypted Stats.txt','w') as stat_file:
            while True:
                text = input_file.read().replace(b'\r',b'')
                if text == b'':
                    break
                str_text = text #
                length = int((len(str(str_text))) / key_size)-2# Get the length of the data divide by key size
                the_key = key_stretch(key,length)
                print("Text ",len(str_text), str_text)
                print("Key: ",len(the_key),the_key)
                output = ''
                j=0
                for j in range(length*key_size-1):
                    xor = hex(str_text[j] ^ the_key[j]) # Xor the two values
                    output += str(xor)[2:].zfill(2) ## omit the first 0x letters from hex
                print(output,file=output_file)

                line_number += 1


output_file.close()
input_file.close()
stat_file.close()
print("Output = ",output)
print("Result = ",result)
print("Compare output with the result = ", result == output)
