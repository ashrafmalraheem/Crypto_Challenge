# Crypto challenge Set 1 No 2
print("Crypto challenge Set 1 No 2")

x = 0x1c0111001f010100061a024b53535009181c
y = 0x686974207468652062756c6c277320657965
answer = 0x746865206b696420646f6e277420706c6179
xor = x ^ y
print("Calculated XOR = ",hex(xor))
print("Obtained XOR   = ",hex(answer))
print("Compare Result = ",(answer == xor))
