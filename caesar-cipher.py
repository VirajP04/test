s = input("Enter the text: ")
key = int(input("Enter the key value: "))
encrypted=""

#encryption
for i in range(0,len(s)):
    ascii_val = ord(s[i])
    if(ascii_val != 32):
        if(ascii_val>96 and ascii_val<123):
            if(ascii_val-32+key>90):
                encrypted+=chr(ascii_val-32+key-26)
            else:
                encrypted+=chr(ascii_val-32+key)
        else:
            encrypted+=chr(ascii_val+key)
print(encrypted)
#decryption
decrypted = ""
for i in range(0,len(encrypted)):
    ascii_val = ord(encrypted[i])
    if(ascii_val != 32):
        if(ascii_val>64 and ascii_val<91):
                decrypted+=chr(ascii_val+32-key)
        else:
            decrypted+=chr(ascii_val-key)
print(decrypted)
    