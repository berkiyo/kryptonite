from Crypto.Cipher import AES
import hashlib

password = 'mypassword'.encode("utf8")
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
init_vector = 'This is an IV456'.encode("utf8")

# Padding the message to meet 32 bit requirement
def message_padding(file):
    while len(file)%16 != 0:
        file = file + b'0'
    return file

cipher = AES.new(key, mode, init_vector)

with open('secret.txt', 'rb') as f:
    original_file = f.read()

padded_message = message_padding(original_file)
encrypted_message = cipher.encrypt(padded_message)

with open('encrypted_data', 'wb') as e:
    e.write(encrypted_message)