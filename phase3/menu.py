from phase3.helpers.encode_decode import fernet_cli
from phase3.helpers.generic_cli import generic_cli


menu = {
    "1": {"message":  "Enocde / Decode message", "func": fernet_cli},
    "2": {"message": "Hash Message"},
    "3": {"message": "Crack Hashed Message"},
    "4": {"message": "Encrypt / Decrypt Message (Symetric)"},
    "5": {"message": "Encrypt / Decrypt Message (Asymetric)"},
    "6": {"message": "Launch chatroom"}
}


def phase3Menu():
    generic_cli(menu=menu)
