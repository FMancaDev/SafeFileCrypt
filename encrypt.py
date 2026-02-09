#!/usr/bin/env python3

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os
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


def encrypt_file(file_path: Path, fernet: Fernet):
    data = file_path.read_bytes()
    encrypted_data = fernet.encrypt(data)
    file_path.write_bytes(encrypted_data)


def main():
    file_name = input("Digite o nome do arquivo para criptografar: ").strip()
    file_path = Path(file_name)

    if not file_path.exists() or not file_path.is_file():
        print("Arquivo não encontrado.")
        return

    confirm = input(
        f"Tem certeza que deseja criptografar '{file_name}'? (sim/não): ").lower()
    if confirm != "sim":
        print("Operação cancelada.")
        return

    password = getpass.getpass("Digite a senha: ")
    password_confirm = getpass.getpass("Confirme a senha: ")

    if password != password_confirm:
        print("As senhas não coincidem.")
        return

    # Gerar salt apenas uma vez
    if not os.path.exists(SALT_FILE):
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
    else:
        salt = open(SALT_FILE, "rb").read()

    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    encrypt_file(file_path, fernet)

    print("Arquivo criptografado com sucesso.")


if __name__ == "__main__":
    main()
