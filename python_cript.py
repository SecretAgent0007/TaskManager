from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import secrets
import hashlib

#Шифруем сообщение методом AES и паролем из трехзначного числа
message = b'I am studen on Netology'
BS = AES.block_size
key = hashlib.sha256(b"265").digest()[:16]
plain_text = pad(message, BS)
iv = secrets.token_bytes(BS)
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = iv + cipher.encrypt(plain_text)
print("Cipher_text:", cipher_text)

#Цикл для метода перебора
for i in range(1000):
    password = str(i).zfill(3)
    key = hashlib.sha256(password.encode()).digest()[:16]
    iv = cipher_text[:BS]
    encrypted_data = cipher_text[BS:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        plain_text = unpad(cipher.decrypt(encrypted_data), BS)
        print(f"Ключ: {password}, Результат: {plain_text.decode()}")
        break
    except ValueError:
        continue
