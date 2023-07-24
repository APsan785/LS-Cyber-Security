from pwn import *
from string import printable

context.log_level = 'critical'

k=0
char_match=0
flag=""

while k < (len(printable)):
        #print("k is "+str(k))
        i = printable[k]
        #print("i is "+str(i))
        p = process("./notwordle")
        p.recv()
        p.sendline(bytes(flag+i, 'utf-8'))
        code = p.recvline()
        #print("decode is "+str(code.decode('UTF-8')))
        #print(code.decode('UTF-8')[0])
        decode_=code.decode('UTF-8')

        slice = decode_[0] if char_match < 10 else decode_[:2]

        if slice != str(char_match):
                print(i)
                flag = flag +i
                print(flag)
                k=0
                char_match+=1
        else :
                k+=1
        if char_match == 30:
                print("Sarvadaa, Your Flag is : "+flag)
                break
        p.close()

print("first letter" + i)
