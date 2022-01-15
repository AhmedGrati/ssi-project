import getpass
import re

from phase12.repository import UserRepository

"""
    Email and password constraints:
       . The user email should follow this regex: first_name.last_name@insat.ucar.tn.
       . The user password and password confirmation should match.
       . The length of the password should be strictly greater than 6 to increase security.
"""


def check_constraints(email: str, password: str, password_confirmation: str):
    email_regex = r"\b[A-Za-z0-9]+\.[A-Za-z0-9]+@insat.ucar.tn\b"
    if (
        re.fullmatch(email_regex, email)
        and password == password_confirmation
        and len(password) > 6
    ):
        return True
    return False


"""
    This function extracts the first_name and the last_name of the user from the email.
    the extracted values will be inserted automatically into database.
"""


def extract_names(email: str):
    first_name, lastname = email.split("@")[0].split(".")
    return first_name, lastname


def sign_up(user_repo: UserRepository):
    print(
        "********************************* Registration **************************************"
    )
    constraints_verified = False
    email = None
    password = None
    while not constraints_verified:
        email = str(input("Enter your email: "))
        password = getpass.getpass("Enter your password: ")
        password_confirmation = getpass.getpass("Enter your password confirmation: ")
        constraints_verified = check_constraints(
            email=email, password=password, password_confirmation=password_confirmation
        )
    first_name, last_name = extract_names(email=email)
    try:
        user_repo.add_user(
            first_name=first_name, last_name=last_name, email=email, password=password
        )
    except:
        print("This user already exists please try another user!")
        sign_up(user_repo=user_repo)


def login(user_repo: UserRepository):
    print(
        "********************************* Login **************************************"
    )
    email = None
    password = None
    while email is None and password is None:
        email = str(input("Enter your email: "))
        password = getpass.getpass("Enter your password: ")

    login_result = user_repo.login(email=email, password=password)
    if login_result is True:
        print("Login Successfully!")
    else:
        print("Please verify your email and password and re-login!")
