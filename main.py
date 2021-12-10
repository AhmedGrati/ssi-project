from db_connector import DBConnector
from repository import UserRepository
import auth
if __name__ == '__main__':
    user_choice = None
    conn = DBConnector.Instance(
        hostname="localhost",
        user="ahmed",
        password="ahmed",
        database="ssi"
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