from Crypto.Cipher import DES
import time
import hashlib

# start the timer
start_time = time.time()

password = 'helloworld'.encode("utf8")
key = hashlib.sha256(password).digest()
mode = DES.MODE_CBC
init_vector = 'This is an IV456'.encode("utf8")

i = 10000     # number of iterations

# loop
for x in range (0, i):
    cipher = DES.new(key, mode, init_vector)


    with open('encrypted_data','rb' ) as e:
        encrypted_data = e.read()

    decrypted_file = cipher.decrypt(encrypted_data)

    with open('decrypted_secret.txt', 'wb') as df:
        df.write(decrypted_file.rstrip(b'0'))


print ("The DES decryption took", time.time() - start_time, "to run")