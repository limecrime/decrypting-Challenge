def decode(encodedMessage):
    message = []
    lencount = []

    for i in encodedMessage:
        lencount.append(i)
        if i.isdecimal():
            message.append(encodedMessage[len(lencount) + int(i) ])

    return ''.join(message)

userMessage = input('Input the message that needs decoding:')

print(decode(userMessage))