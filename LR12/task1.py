from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except:
        return False

def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, "wb") as file:
        file.write(data)


# Генерация ключевой пары
private_key, public_key = generate_key_pair()

# Чтение файла, который нужно подписать
file_path = "test.txt"
message = read_file(file_path)

# Подписание файла
signature = sign_message(private_key, message)

# Запись подписи в файл
signature_file_path = "signature.sig"
write_file(signature_file_path, signature)

# Проверка подписи
signature_to_verify = read_file(signature_file_path)
is_valid_signature = verify_signature(public_key, message, signature_to_verify)
if is_valid_signature:
    print("Подпись верна.")
else:
    print("Подпись неверна.")
