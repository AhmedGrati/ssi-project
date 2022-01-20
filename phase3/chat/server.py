import datetime
import os
import socket
import threading
import time
from random import randbytes

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from termcolor import colored

time.clock = time.time


class Server:
    def __init__(self, port):

        self.host = "127.0.0.1"
        self.port = port

    def start_server(self):

        # Generate the public and private keys to share
        # And a random secret key for AES
        self.generate_keys()
        secret_key = randbytes(16)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.clients = []

        self.s.bind((self.host, self.port))
        self.s.listen(100)

        print(colored("[+] Running on host: " + str(self.host), "yellow"))
        print(colored("[+] Running on port: " + str(self.port), "yellow"))

        self.username_lookup = {}

        while True:
            c, addr = self.s.accept()
            username = c.recv(1024).decode()
            print(colored("[+] New connection. Username: " + str(username), "yellow"))
            self.broadcast(
                colored(" New person joined the room. Username: " + username, "yellow")
            )
            self.username_lookup[c] = username
            self.clients.append(c)
            client_pub_key = self.send_pub_key(
                c
            )  # Exchange the public key with the client
            encrypted_secret = self.encrypt_secret(
                client_pub_key, secret_key
            )  # Encrypt the secret with the client public key
            self.send_secret(
                c, encrypted_secret
            )  # send the encrypted secret to the client
            threading.Thread(
                target=self.handle_client,
                args=(
                    c,
                    addr,
                ),
            ).start()

    ##### Sending broadcast messages
    def broadcast(self, msg):
        for connection in self.clients:
            print(colored("[+] Broadcast message: " + msg, "red"))

    ##### Generate the public and private key pair
    def generate_keys(self):
        try:
            private_key = RSA.generate(2048)
            public_key = private_key.publickey()
            private_key_pem = private_key.exportKey().decode()
            public_key_pem = public_key.exportKey().decode()
            with open("server_private_key.pem", "w+") as priv:
                priv.write(private_key_pem)
            with open("server_public_key.pem", "w+") as pub:
                pub.write(public_key_pem)
            return public_key

        except Exception as e:
            print(e)

    ##### Encrypt the secret with the client public key
    def encrypt_secret(self, client_pub_key, secret_key):
        try:
            cpKey = RSA.importKey(client_pub_key)
            cipher = PKCS1_OAEP.new(cpKey)
            encrypted_secret = cipher.encrypt(secret_key)
            return encrypted_secret

        except Exception as e:
            print(e)

    def send_secret(self, c, secret_key):
        try:
            c.send(secret_key)
            print(colored("[+] Secret key had been sent to the client", "yellow"))

        except Exception as e:
            print(e)

    ##### Exchanging the public key with the client
    def send_pub_key(self, c):
        try:
            public_key = RSA.importKey(open("server_public_key.pem", "r").read())
            c.send(public_key.exportKey())
            client_pub_key = c.recv(1024)
            print(colored("[+] Client public key had been received", "yellow"))
            return client_pub_key

        except Exception as e:
            print(e)

    def handle_client(self, c, addr):
        while True:
            try:
                msg = c.recv(1024)
            except:
                c.shutdown(socket.SHUT_RDWR)
                self.clients.remove(c)
                self.broadcast(str(self.username_lookup[c]) + " has left.")
                break

            if msg.decode() != "":
                current_time = datetime.datetime.now()
                print(
                    colored(
                        current_time.strftime("%Y-%m-%d %H:%M:%S")
                        + " Mesage exchanged",
                        "blue",
                    )
                )
                for connection in self.clients:
                    if connection != c:
                        connection.send(msg)
            else:
                print(
                    colored(
                        "[+] " + self.username_lookup[c] + " left the server.", "red"
                    )
                )
                for conn in self.clients:
                    if conn == c:
                        self.clients.remove(c)
                break


def terminate(Server):
    while True:
        command = input("")
        if command == "TERMINATE":
            for conn in Server.clients:
                conn.shutdown(socket.SHUT_RDWR)
            print(colored("[+] All connections had been terminated", "yellow"))
        break
    print(colored("[+] Server is shut down", "yellow"))
    os._exit(0)


if __name__ == "__main__":

    server = Server(5555)
    terminate = threading.Thread(target=terminate, args=(server,))
    terminate.start()
    server.start_server()
