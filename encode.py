def encrypt():
    with open("flag.txt", 'r') as file:
        flag=file.read()
    it = 1
    cha = 1
    enc=""
    for i in flag:
        i = chr((ord(i) + it) ^ ord(chr(abs(it-cha))))
        it+=cha; cha+=1
        enc+=i
    with open("flag.txt", 'w') as file:
        file.write(enc)

encrypt()