from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def save_private_key(private_key, filename):
    with open(filename, "wb") as key_file:
        key_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

def load_private_key(filename):
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def encrypt_message(public_key, message):
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()), # маскирующая функция генерации
            algorithm=hashes.SHA256(), # хэш функция
            label=None # используется для передачи аутентификационных данных
        )
    )
    return ciphertext

def decrypt_message(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

# Генерация ключевой пары
private_key, public_key = generate_key_pair()

# Сохранение закрытого ключа в файл
save_private_key(private_key, "private_key.pem")

# Загрузка закрытого ключа из файла
loaded_private_key = load_private_key("private_key.pem")

# Шифрование и расшифрование сообщения
message = input("Введите сообщение для шифрования: ")
encrypted_message = encrypt_message(public_key, message)
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = decrypt_message(loaded_private_key, encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
