from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from os import urandom

def encrypt_aes_ofb(key, iv, plaintext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.OFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder() # используется для дополения текста до необходимой длинны, PKCS7(128)- для согласованности длины блоков
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return ciphertext

def decrypt_aes_ofb(key, iv, ciphertext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.OFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(decrypted_padded_plaintext) + unpadder.finalize()
    return plaintext

# Пример использования

# Генерация ключа и вектора инициализации
key = urandom(32)  # 256-bit ключ
iv = urandom(16)   # 128-bit вектор инициализации

# Текст, который нужно зашифровать
plaintext = b"Hello, world!"

# Шифрование
ciphertext = encrypt_aes_ofb(key, iv, plaintext)
print("Зашифрованный текст:", ciphertext)

# Расшифрование
decrypted_plaintext = decrypt_aes_ofb(key, iv, ciphertext)
print("Расшифрованный текст:", decrypted_plaintext.decode())
