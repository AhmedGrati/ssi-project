class User:
    id: int
    email: str
    first_name: str
    last_name: str
    password: str

    def __init__(self, query_result):
        self.id = query_result[0]
        self.first_name = query_result[1]
        self.last_name = query_result[2]
        self.email = query_result[3]
        self.password = query_result[4]
