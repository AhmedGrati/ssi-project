from phase3.helpers.generic_cli import generic_cli


def encode_bytes():
    message = input("Enter Message to be encoded into Bytes: ")
    print(f'Encoded Message:\n{message.encode("utf-8").hex()}\n')


def decode_bytes():
    message = input("Enter Message to be decoded from Bytes: ")
    word = bytes.fromhex(message).decode("utf-8")
    print(f"Decoded Message:\n{word}\n")


menu = {
    "a": {"message": "Enocde Message", "func": encode_bytes},
    "b": {"message": "Decode Message", "func": decode_bytes},
}


def encode_cli():
    generic_cli(menu=menu)
