from Crypto.Cipher import AES
import hashlib

password = "mypassword".encode()
key = hashlib.sha256(password).digest()
initVector = "This is an IV456"

# Padding the message to meet 32 bit requirement
def messagePadding(message):
    while len(message)%16 != 0:
        message = message + " "
    return message

#cipher = AES.new(key, mode, initVector)
message = "this is my super secret password"
paddedMessage = messagePadding(message)

print(len(paddedMessage))