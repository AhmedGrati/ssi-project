from typing import Any, Dict


def generic_cli(menu: Dict[str, Dict[str, Any]]):
    start_message = (f'{key} - {value["message"]}' for key, value in menu.items())
    menu_text = "\n".join(start_message)

    choice = -1
    while choice not in menu:
        choice = input(f"\nEnter your choice:\n{menu_text}\n")
        if choice not in menu:
            print("\nInvalid choice")

    menu[choice]["func"]()
