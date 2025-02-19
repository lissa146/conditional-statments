message = input("give me a message to encrypt ")

shift = int(input("give me a number of positions to shift "))

EMessage = ""


for i in message:
    if message.isupper():
        EMessage += chr((ord(i) + shift - ord('A')) % 26 + ord('A'))

    else:
        EMessage += chr((ord(i) + shift - ord('Z')) % 26 + ord('Z'))

print(EMessage)
