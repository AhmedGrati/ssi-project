import phase3.chat.client as client
import phase3.chat.server as server
from phase3.helpers.generic_cli import generic_cli

menu = {
    "a": {"message": "Run client", "func": client.run_client},
    "b": {"message": "Run server", "func": server.run_server},
}


def chat_room_cli():
    generic_cli(menu=menu)
