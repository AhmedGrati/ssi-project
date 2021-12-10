import os

from db_connector import DBConnector
from repository import UserRepository
import auth
from dotenv import load_dotenv

load_dotenv(".env")
if __name__ == '__main__':
    user_choice = None
    DB_HOSTNAME: str = os.environ.get("DB_HOSTNAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_DATABASE: str = os.environ.get("DB_DATABASE")
    conn = DBConnector.Instance(
        hostname=DB_HOSTNAME,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )
    user_repo = UserRepository(db_connector=conn)
    while user_choice != 4:
        user_choice = int(input("Enter your choice: \n"
                                "1. To register a new user.\n"
                                "2. To login a user.\n"
                                "3. To Go to phase3.\n"
                                "4. To quit.\n"))
        if user_choice == 1:
            auth.sign_up(user_repo=user_repo)
            print()
            print()
        elif user_choice == 2:
            auth.login(user_repo=user_repo)
            print()
            print()
        elif user_choice == 3:
            # TODO: Wadhah implements phase 3
            print("PHASE 3")