import rsa

from phase3.helpers.generic_cli import generic_cli

pubkey, privkey = rsa.newkeys(512)


def pad(text: str, modulo: int):
    n = len(text) % modulo
    return text.encode() + (b" " * (modulo - n))


def encrypt_rsa(key, message: str) -> str:
    crypto: bytes = rsa.encrypt(message.encode(), key)
    return crypto.hex()


def encrypt_rsa_cli():
    message = input("Enter Message to be encrypted RSA: ")
    enc_message = encrypt_rsa(key=pubkey, message=message)
    print(f"Encrypted Message:\n{enc_message}\n")


def encrypt_Elgamal_cli():
    return


def decrypt_rsa(key, message: str) -> str:
    crypto: bytes = rsa.decrypt(bytes.fromhex(message), key)
    return crypto.decode("utf-8").strip()


def decrypt_ras_cli():
    message = input("Enter Message to be decrypted RSA: ")
    dec_message = decrypt_rsa(key=privkey, message=message)
    print(f"Encrypted Message:\n{dec_message}\n")
    return


def decrypt_Elgamal_cli():
    return


menu = {
    "a": {"message": "Encrypt Message RSA", "func": encrypt_rsa_cli},
    "b": {"message": "Encrypt Message Elgamal", "func": encrypt_Elgamal_cli},
    "c": {"message": "Decrypt Message RSA", "func": decrypt_ras_cli},
    "d": {"message": "Decrypt Message Elgamal", "func": decrypt_Elgamal_cli},
}


def encrypt_asym_cli():
    generic_cli(menu=menu)
