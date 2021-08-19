from Crypto.Cipher import AES
import time
import hashlib

# start the timer
start_time = time.time()

password = 'helloworld'.encode("utf8")
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
init_vector = 'This is an IV456'.encode("utf8")
i = 10000     # number of iterations

# Padding the message to meet 128 bit requirement
def message_padding(file):
    while len(file)%16 != 0:
        file = file + b'0'
    return file

for x in range (0, i):
    cipher = AES.new(key, mode, init_vector)

    # loop
    #for x in range (0, i):
        # open the file
    with open('secret.txt', 'rb') as f:
        original_file = f.read()    

    # make the file encryptable
    padded_message = message_padding(original_file)
    encrypted_message = cipher.encrypt(padded_message)

    # write the message to the file "encrypted_data"
    with open('encrypted_data', 'wb') as e:
        e.write(encrypted_message)

print ("The AES encryption took", time.time() - start_time, "to run")