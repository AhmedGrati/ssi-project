import random

from passlib.hash import sha512_crypt

from phase12.db_connector import DBConnector
from phase12.email_service import EmailService
from phase12.user import User


class UserRepository:
    db_connector: DBConnector = None
    email_service: EmailService = None

    def __init__(self, db_connector, email_service):
        self.db_connector = db_connector
        self.email_service = email_service
        self.create_table()

    def create_table(self):
        cursor = self.db_connector.db_connection.cursor()
        cursor.execute("SHOW TABLES")
        table_exists = False
        for tables in cursor:
            for table in tables:
                if table == "users":
                    table_exists = True
                    break
        if table_exists is not True:
            cursor.execute(
                "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255)"
                ", email VARCHAR(255), password VARCHAR(255))"
            )

    def add_user(self, first_name: str, last_name: str, email: str, password: str):
        if self.get_user_by_email(email=email) is None:
            insert_user_query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
            values = (first_name, last_name, email, sha512_crypt.hash(password))
            cursor = self.db_connector.db_connection.cursor()
            cursor.execute(insert_user_query, values)
            self.db_connector.db_connection.commit()
        else:
            raise Exception("This user already exists please try another user")

    def get_user_by_email(self, email: str):
        get_user_by_email_query = "SELECT * FROM users where email = %s"
        user_email = (email,)
        cursor = self.db_connector.db_connection.cursor()
        cursor.execute(get_user_by_email_query, user_email)
        return cursor.fetchone()

    def login(self, email: str, password: str):
        result = self.get_user_by_email(email=email)
        random_number = random.randint(100000, 999999)
        if result is None:
            return False
        user = User(query_result=result)
        pass_verification = sha512_crypt.verify(password, user.password)
        if pass_verification is True:
            content = f"Code: {random_number}"
            self.email_service.send_email(receiver_email=user.email, content=content)
            verification_code = int(input("Enter your verification code:"))
            if verification_code == random_number:
                return True
            return False
