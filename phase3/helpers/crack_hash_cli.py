import hashlib

from phase3.helpers.generic_cli import generic_cli


def get_password_list_generator():
    with open("./phase3/assets/passwords.txt", "r") as f:
        for i in f.readlines():
            yield (i)


def crack_md5_cli():
    message = input("Enter Message to be cracked MD5: ")
    for i in get_password_list_generator():
        if hashlib.md5(i.strip().encode()).hexdigest() == message:
            print(f"\ncracked Message:\n{i}\n")
            return

    print(f"\nCould Not find message in password list\n")


def crack_sh1_cli():
    message = input("Enter Message to be cracked SH1: ")
    for i in get_password_list_generator():
        if hashlib.sha1(i.strip().encode()).hexdigest() == message:
            print(f"\ncracked Message:\n{i}\n")
            return

    print(f"\nCould Not find message in password list\n")


def crack_sha256_cli():
    message = input("Enter Message to be cracked SH256")
    for i in get_password_list_generator():
        if hashlib.sha256(i.strip().encode()).hexdigest() == message:
            print(f"\ncracked Message:\n{i}\n")
            return

    print(f"\nCould Not find message in password list\n")


menu = {
    "a": {"message": "Crack Md5", "func": crack_md5_cli},
    "b": {"message": "Crack SH1", "func": crack_sh1_cli},
    "c": {"message": "Crack SHA256", "func": crack_sha256_cli},
}


def crack_hash_cli():
    generic_cli(menu=menu)
