from phase3.helpers.crack_hash_cli import crack_hash_cli
from phase3.helpers.encode_decode import encode_cli
from phase3.helpers.encrypt_asym import encrypt_asym_cli
from phase3.helpers.encrypt_sym import encrypt_sym_cli
from phase3.helpers.generic_cli import generic_cli
from phase3.helpers.hash_cli import hash_cli

menu = {
    "1": {"message": "Enocde / Decode message", "func": encode_cli},
    "2": {"message": "Hash Message", "func": hash_cli},
    "3": {"message": "Crack Hashed Message", "func": crack_hash_cli},
    "4": {"message": "Encrypt / Decrypt Message (Symetric)", "func": encrypt_sym_cli},
    "5": {"message": "Encrypt / Decrypt Message (Asymetric)", "func": encrypt_asym_cli},
    "6": {"message": "Launch chatroom"},
}


def phase3Menu():
    generic_cli(menu=menu)
