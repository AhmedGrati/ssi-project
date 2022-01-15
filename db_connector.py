from singleton import Singleton
import mysql.connector


@Singleton
class DBConnector(object):
    db_connection = None

    def __init__(self, hostname, user, password, database):
        self.db_connection = mysql.connector.connect(
            host=hostname, user=user, password=password, database=database
        )

    def __str__(self):
        return "Database connection object"
