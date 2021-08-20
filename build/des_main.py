# Berk Dogan - DES Encryptor and Decryptor (speedtest)

#   GOALS
#       -> Encrypt a text file with a secret key (see the "password" variable)
#       -> Decrypt a text file with a secret key
#       -> Time how long it takes after 10000 iterations
#       -> Compare this to DES encryption

# This code is for a university course, released under GPL v3 license. 

from Crypto.Cipher import DES
import time
import hashlib

# start the timer
start_time = time.time()

key = b'-8B key-'
mode = DES.MODE_OFB
i = 50000     # number of iterations

# Padding the message to meet 128 bit requirement
def message_padding(file):
    while len(file)%16 != 0:
        file = file + b'0'
    return file

def encrypt():
    for x in range (0, i):
        cipher = DES.new(key, mode)

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

def decrypt():
    for x in range (0, i):
        cipher = DES.new(key, mode)


        with open('encrypted_data','rb' ) as e:
            encrypted_data = e.read()

        decrypted_file = cipher.decrypt(encrypted_data)

        with open('decrypted_secret.txt', 'wb') as df:
            df.write(decrypted_file.rstrip(b'0'))
    print ("The DES decryption took", time.time() - start_time, "to run")

encrypt()
decrypt()