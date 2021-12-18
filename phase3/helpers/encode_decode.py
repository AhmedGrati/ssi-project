from cryptography.fernet import Fernet
from phase3.helpers.generic_cli import generic_cli


def encryp_fernet():
    print("")


def decrypt_fernet():
    print("")


menu = {
    "a": {"message":  "Enocde Message", "func": encryp_fernet},
    "b": {"message": "Decode Message", "func": decrypt_fernet},
}


def fernet_cli():
    generic_cli(menu=menu)
