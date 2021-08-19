from Crypto.Cipher import DES
import time
import hashlib

# start the timer
start_time = time.time()

password = 'helloyou'.encode("utf8")
key = hashlib.sha256(password)
mode = DES.MODE_CBC
init_vector = 'helloyou'.encode("utf8")
i = 10000     # number of iterations

# Padding the message to meet 56 bit requirement
def message_padding(file):
    while len(file)%7 != 0:
        file = file + b'0'
    return file

for x in range (0, i):
    cipher = DES.new(password, mode, init_vector)

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

print ("The DES encryption took", time.time() - start_time, "to run")