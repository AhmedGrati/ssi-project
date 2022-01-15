import rsa

from elgamal import elgamal
from phase3.helpers.generic_cli import generic_cli

rsa_pubkey, rsa_privkey = rsa.newkeys(512)

_elgamal_keys = elgamal.generate_keys(128)
elgamal_pubkey = _elgamal_keys["publicKey"]
elgamal_privkey = _elgamal_keys["privateKey"]


def pad(text: str, modulo: int):
    n = len(text) % modulo
    return text.encode() + (b" " * (modulo - n))


def encrypt_rsa(key, message: str) -> str:
    crypto: bytes = rsa.encrypt(message.encode(), key)
    return crypto.hex()


def encrypt_elgamal(key, message: str) -> str:
    crypto = elgamal.encrypt(key, message)
    return crypto


def encrypt_rsa_cli():
    message = input("Enter Message to be encrypted RSA: ")
    enc_message = encrypt_rsa(key=rsa_pubkey, message=message)
    print(f"Encrypted Message RSA:\n{enc_message}\n")


def encrypt_elgamal_cli():
    message = input("Enter Message to be encrypted RSA: ")
    enc_message = encrypt_elgamal(key=elgamal_pubkey, message=message)
    print(f"Encrypted Message Elgamal:\n{enc_message}\n")


def decrypt_rsa(key, message: str) -> str:
    crypto: bytes = rsa.decrypt(bytes.fromhex(message), key)
    return crypto.decode("utf-8").strip()


def decrypt_rsa_cli():
    message = input("Enter Message to be decrypted RSA: ")
    dec_message = decrypt_rsa(key=rsa_privkey, message=message)
    print(f"Decrypted RSA Message:\n{dec_message}\n")


def decrypt_elgamal(key, message: str) -> str:
    crypto = elgamal.decrypt(key=key, cipher=message)
    return crypto


def decrypt_Elgamal_cli():
    message = input("Enter Message to be decrypted RSA: ")
    dec_message = decrypt_elgamal(key=elgamal_privkey, message=message)
    print(f"Decrypted Elgamal Message:\n{dec_message}\n")


menu = {
    "a": {"message": "Encrypt Message RSA", "func": encrypt_rsa_cli},
    "b": {"message": "Encrypt Message Elgamal", "func": encrypt_elgamal_cli},
    "c": {"message": "Decrypt Message RSA", "func": decrypt_rsa_cli},
    "d": {"message": "Decrypt Message Elgamal", "func": decrypt_Elgamal_cli},
}


def encrypt_asym_cli():
    generic_cli(menu=menu)
