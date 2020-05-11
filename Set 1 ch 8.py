
def find_match(cipher_text):
    keylength = 16
    for k in range(int(len(cipher_text))):
        for l in range(int(len(cipher_text[0])/keylength)):
            block1 = cipher_text[k][(l)*keylength:(l+1)*keylength]
            #print(len(block1),block1)
            count_match = 0
            #match_location = [(,)]
            for i in range(int(len(cipher_text))):
                for j in range(int(len(cipher_text[i])/keylength)):
                    #if hamming_distance(block1,cipher_text[i][j*keylength:(j+1)*keylength]) == 0:
                    if block1 == cipher_text[i][j*keylength:(j+1)*keylength]:
                        if j != l:
                            print("Find Match! in line",i,'Block',j)



from Crypto.Cipher import AES
from base64 import b64decode




cipher_bytes = []
with open('8.txt', 'r') as input_file:
    while True:
        cipher_text = input_file.readline().rstrip('\n')
        if cipher_text == '':
            break
        cipher_bytes.append(int(cipher_text,16).to_bytes(int(len(cipher_text)/2),'big'))
print(len(cipher_bytes[0]))
find_match(cipher_bytes)

line_ecb = cipher_bytes[132]

for i in range(10):
    print(i,line_ecb[i*16:(i+1)*16])