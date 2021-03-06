import argparse
import datetime
import json
import os
import random
import socket
import string
import threading
import time
from base64 import b64decode, b64encode

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from termcolor import colored

time.clock = time.time


def pad(text: str, modulo: int):
    n = len(text) % modulo
    return text.encode() + (b" " * (modulo - n))


class Client:
    def __init__(self, server, port, username):
        self.server = server
        self.port = port
        self.username = username

    ###### Create the connection to the server
    def create_connection(self):
        ###### Setting up the socket, takes the serverIP and portNumber arguments to set up the connection to the server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.server, self.port))
        except Exception as e:
            print(e)
            # print(colored("[!] " + e, "red"))

        ####### Initial message exchanges for the communication
        ####### Setting up username, keys
        ####### Calling exchange secret and pub key functions

        self.s.send(
            self.username.encode()
        )  # Inform the server about the username connected
        print(colored("[+] Connected successfully", "yellow"))
        print(colored("[+] Exchanging keys", "yellow"))

        self.create_key_pairs()  # Create key pairs
        self.exchange_public_keys()  # Initial public key exchange
        global secret_key  # Global variable to hold the secret key for AES encryption
        secret_key = (
            self.handle_secret()
        )  # Function to get the secret generated by the server

        print(colored("[+] Initial set up had been completed!", "yellow"))
        print(colored("[+] Now you can start to exchange messages", "yellow"))

        ####### InputHandle for sending messages and MessageHandle thread for receiving messages
        message_handler = threading.Thread(target=self.handle_messages, args=())
        message_handler.start()
        input_handler = threading.Thread(target=self.input_handler, args=())
        input_handler.start()

    ####### Handle receiving messages
    def handle_messages(self):
        while True:
            message = self.s.recv(1024).decode()
            if message:
                key = secret_key
                decrypt_message = json.loads(message)
                cipherText = b64decode(decrypt_message["ciphertext"])
                cipher = AES.new(
                    key,
                    AES.MODE_ECB,
                )
                msg = cipher.decrypt(cipherText)
                current_time = datetime.datetime.now()
                print(
                    colored(
                        current_time.strftime("%Y-%m-%d %H:%M:%S ") + msg.decode(),
                        "green",
                    )
                )
            else:
                print(colored("[!] Lost the connection to the server", "red"))
                print(colored("[!] Closing down the connection", "red"))
                self.s.shutdown(socket.SHUT_RDWR)
                os._exit(0)

    ####### Handle user input and send message
    def input_handler(self):
        while True:
            message = input()  # Take the input from the user
            if message == "EXIT":  # EXIT will close down the client
                break
            else:
                key = secret_key
                cipher = AES.new(key, AES.MODE_ECB)
                message_to_encrypt = self.username + ": " + message

                message_to_encrypt = pad(message_to_encrypt, 16)

                msgBytes = message_to_encrypt  # Byte encode it, because AES input must be byte encoded
                encrypted_message = cipher.encrypt(msgBytes)  # Encrypt the message
                # iv = b64encode(cipher.iv).decode(
                #     "utf-8"
                # )  # Generate the initialization vector, b64encode it, than utf-8 representation to send
                message = b64encode(encrypted_message).decode(
                    "utf-8"
                )  # Same process to the encrypted message, to overcome special chars
                result = json.dumps(
                    {"ciphertext": message}
                )  # Insert it into a json dictionary
                self.s.send(result.encode())  # Send it in byte encoded form

        self.s.shutdown(socket.SHUT_RDWR)
        os._exit(0)

    ###### Receiving the secret key for symmetric encryption
    def handle_secret(self):
        secret_key = self.s.recv(
            1024
        )  # The secret key coming from the server, and used for encryption and decryption
        private_key = RSA.importKey(
            open("client_private_key.pem", "r").read()
        )  # Import the client private key to decrypt the secret
        cipher = PKCS1_OAEP.new(
            private_key
        )  # Using the client private key to decrypt the secret
        return cipher.decrypt(secret_key)

    ###### Send the public key to the server to encrypt the secret
    ###### The secret is generated by the server and used for symmetric encryption
    def exchange_public_keys(self):
        try:
            print(colored("[+] Getting public key from the server", "blue"))
            server_public_key = self.s.recv(1024).decode()
            server_public_key = RSA.importKey(server_public_key)

            print(colored("[+] Sending public key to server", "blue"))
            public_pem_key = RSA.importKey(open("client_public_key.pem", "r").read())
            self.s.send(public_pem_key.exportKey())
            print(colored("[+] Exchange completed!", "yellow"))

        except Exception as e:
            print(colored("[!] ERROR, you messed up something.... " + e, "red"))

    ###### Generate public and private key pairs
    def create_key_pairs(self):
        try:
            private_key = RSA.generate(2048)
            public_key = private_key.publickey()
            private_pem = private_key.exportKey().decode()
            public_pem = public_key.exportKey().decode()
            with open(
                "client_private_key.pem", "w"
            ) as priv:  # writing priv key to pem file
                priv.write(private_pem)
            with open(
                "client_public_key.pem", "w"
            ) as pub:  # writing public key to pem file
                pub.write(public_pem)

        except Exception as e:
            print(colored("[!] ERROR, you messed up somethig.... " + e, "red"))


if __name__ == "__main__":
    username = input("Enter Your username : ")
    client = Client("127.0.0.1", 5555, username)
    client.create_connection()
