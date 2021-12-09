class User:
    email: str
    first_name: str
    last_name: str
    password: str

    def __init__(self, email: str, first_name: str, last_name: str, password: str):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
