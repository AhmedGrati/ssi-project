from db_connector import DBConnector
from repository import UserRepository
if __name__ == '__main__':
    print("Hello World")
    conn = DBConnector.Instance(
        hostname="localhost",
        user="ahmed",
        password="ahmed",
        database="ssi"
    )
    user_repo = UserRepository(db_connector=conn)
    user_repo.add_user(
        first_name="Ahmed",
        last_name="Grati",
        email="ahmed.grati@insat.ucar.tn",
        password="ahmed"
    )
    print(user_repo.get_user_by_email(email="ahmed.grati@insat.ucar.tn"))


