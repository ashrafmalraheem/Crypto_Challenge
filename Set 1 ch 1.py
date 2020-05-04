import base64
# Crypto challenge Set 1 Challenge 1
print("Crypto challenge Set 1 Challenge 1")
inputs     = 0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
hex_inputs = inputs
Decoded_answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
print(type(hex_inputs))
print(hex(hex_inputs))
length = int((len(str(hex(hex_inputs)))-2)/2)
print("Length=",(2 * length))
byte_inputs = hex_inputs.to_bytes(length,'big')
print("Without Encoding",byte_inputs)
print("Decrypted Text =",str(byte_inputs, 'utf-8'))
new_base = base64.b64encode(byte_inputs)
output = str(new_base , 'utf-8')
answer = output == Decoded_answer
print("Calculated Base 64= ",output)
print("Obtained Base 64=   ",Decoded_answer)
print("Compare the Two results  = ",answer)
