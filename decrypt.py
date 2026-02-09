#!/usr/bin/env python3

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
from pathlib import Path
import getpass

SALT_FILE = "salt.bin"


def generate_key_from_password(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend(),
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def decrypt_file(file_path: Path, fernet: Fernet):
    data = file_path.read_bytes()
    decrypted_data = fernet.decrypt(data)
    file_path.write_bytes(decrypted_data)


def main():
    file_name = input(
        "Digite o nome do arquivo para descriptografar: ").strip()
    file_path = Path(file_name)

    if not file_path.exists() or not file_path.is_file():
        print("Arquivo não encontrado.")
        return

    if not Path(SALT_FILE).exists():
        print("Arquivo salt.bin não encontrado.")
        return

    password = getpass.getpass("Digite a senha: ")
    salt = Path(SALT_FILE).read_bytes()

    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    try:
        decrypt_file(file_path, fernet)
        print("Arquivo descriptografado com sucesso.")
    except InvalidToken:
        print("Senha incorreta ou arquivo inválido.")


if __name__ == "__main__":
    main()
