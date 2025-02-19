import enchant
d = enchant.Dict("en_US")

message = input("give me a message to encrypt ")

#shift = int(input("give me a number of positions to shift "))

DMessage = ""


for i in range(1, 26):
    for j in message:
        if message.isupper():
            #print(ord(i))
            DMessage += chr((ord(j) - ord('A') - i) % 26 + ord('A'))
            if d.check(DMessage):
                print(DMessage, " is a word")

        else:
            #EMessage += chr((ord(i) + shift - ord('Z')) % 26 + ord('Z'))
            DMessage += chr(((ord(j) - ord('a') - i) % 26) + ord('a'))
            if d.check(DMessage):
                print(DMessage, " is a word")
