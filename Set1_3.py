import base64
# Crypto challenge Set 1 Challenge 3
print("Crypto challenge Set 1 Challenge 3")
def Fixed_XOR(param1,param2):
    return param1 ^ param2


x = 0x20 #  space letter
y = 0x78 #  this is has a 6 time frequency in the decrypted text 
answer = 0x746865206b696420646f6e277420706c6179
an = Fixed_XOR(x,y)
print("The Key should = ",hex(Fixed_XOR(x,y)))
inputs     = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
the_key    = 0x58585858585858585858585858585858585858585858585858585858585858585858
hex_inputs = Fixed_XOR(inputs,the_key)
Decoded_answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
print(hex(hex_inputs))
length = int((len(str(hex(hex_inputs)))-2)/2)
print("Length=",(2 * length))
byte_inputs = hex_inputs.to_bytes(length,'big')
print("Decrypted Text =",str(byte_inputs, 'utf-8'))
print("The Key used   =",hex(the_key))
new_base = base64.b64encode(byte_inputs)
output = str(new_base , 'utf-8')

