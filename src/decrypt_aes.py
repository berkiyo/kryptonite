from Crypto.cipher import AES
import hashlib

password = 'mypassword'
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
IV = 'This is an IV456'

cipher = AES.new(key, mode, IV)

decryptedText = cipher.decrypt()
print