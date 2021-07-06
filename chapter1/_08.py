import re

def cipher(x):
    cipher = {}
    judge = re.compile("[a-z]")
    temp = list(x)
    temp_encode = [ord(n) if judge.search(n) else n for n in temp ]
    encode = [str(n) if type(n) == int else n for n in temp_encode ]
    decode = [chr(n) if type(n) == int else n for n in temp_encode ]
    cipher["encode"] = "-".join(encode)
    cipher["decode"] = "".join(decode)
    return cipher
    
print(cipher("abcd1eg"))


