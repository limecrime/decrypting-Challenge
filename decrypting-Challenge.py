def decode(encodedMessage):
    message = ''
    lencount = 0

    for i in encodedMessage:
        lencount += 1
        if i.isdecimal():
            message += encodedMessage[(lencount + int(i))]

    return message

userMessage = input('Input the message that needs decoding:')

print(decode(userMessage))