def decode(encryption):
    decodedMess = []
    lencount = []

    for i in encryption:
        lencount.append(i)
        if i.isdecimal():
            decodedMess.append(encryption[len(lencount) + int(i) ])

    return ''.join(decodedMess)

encryptedMess = input('Input the message that needs decoding:')

print(decode(encryptedMess))