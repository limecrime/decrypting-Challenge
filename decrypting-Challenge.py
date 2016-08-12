def decode(encryption):
    decodedMess = []

    for i in encryption:
        if i.isdecimal():
            decodedMess.append(encryption[int(i) + 1])

    return ''.join(decodedMess)

encryptedMess = input('Input the message that needs decoding:')

print(decode(encryptedMess))