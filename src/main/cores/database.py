from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector import connect


class Database:
    def __init__(self, conn:CMySQLConnection, database_name):
        self.conn = conn
        self._database_name = database_name

        self._create_database_if_not_exist()
        self._connect_to_the_database()

    def _connect_to_the_database(self):
        self.conn.database = self._database_name

    def _create_database_if_not_exist(self):
        cursor = self.conn.cursor()
        cursor.execute("SHOW DATABASES")

        databases = cursor.fetchall()

        if (self._database_name, ) not in databases:
            cursor.execute(f"CREATE DATABASE {self._database_name}") 
