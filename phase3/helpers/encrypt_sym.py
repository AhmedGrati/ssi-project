from phase3.helpers.generic_cli import generic_cli
from Crypto.Cipher import DES, AES


def pad(text, modulo):
    n = len(text) % modulo
    return text + (b' ' * n)


def encrypt_des_cli():
    key = input("Please Enter Key : ")
    message = input("Enter Message to be encrypted DES: ")
    des = DES.new(key.encode(), DES.MODE_ECB)
    padded_text = pad(message.encode(), 8)
    encrypted_text: bytes = des.encrypt(padded_text)
    print(f'Encoded Message:\n{encrypted_text}\n')


def encrypt_aes256():
    key = input("Please Enter Key : ")
    message = input("Enter Message to be encrypted AES256: ")
    padded_text = pad(message.encode(), 16)
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded_text)
    print(f'Encoded Message:\n{ciphertext}\n')


menu = {
    "a": {"message":  "Encrypt Message DES", "func": encrypt_des_cli},
    "b": {"message": "Encrypt Message AES256", "func": encrypt_aes256},
}


def encrypt_sym_cli():
    generic_cli(menu=menu)
