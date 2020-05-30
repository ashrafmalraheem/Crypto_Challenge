
def validate_PKCS(input,pad=b'\x04'):
    strip = input.replace(pad,b'')
    for i in range(9):
        if strip.find(i.to_bytes(1,'big')) >0:
            print('\nNon valid padding:')
            return None
    return strip

	
test_text = b'ICE ICE BABY\x04\x04\x04\x04'
print(test_text,validate_PKCS(test_text))
test_text = b'ICE ICE BABY\x05\x05\x05\x05'
print(test_text,validate_PKCS(test_text))
test_text = b'ICE ICE BABY\x01\x02\x03\x04'
print(test_text,validate_PKCS(test_text))