def encrypt(text,s):
    result1=""
    for i in range(len(text)):
        char=text[i]
        if char.isupper():
            result1 += chr((ord(char) + s-65) % 26 + 65)
        elif char.islower():
            result1 += chr((ord(char) + s-97) % 26 + 97)
        else:
            result1 += char
    return result1

def decrypt(c,s):
    result2=""
    for i in range(len(c)):
        char=c[i]
        if char.isupper():
            result2 += chr((ord(char) - s-65) % 26 + 65)
        elif char.islower():
            result2 += chr((ord(char) - s-97) % 26 + 97)
        else:
            result2 += char
    return result2

##########################

text=input("Enter text ")
s=int(input("Enter shift value "))
c=encrypt(text,s)
d=decrypt(c,s)
print("Encrypted text is: ",c)    
print("Decrypted text is: ",d)

