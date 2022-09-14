import unittest 
from unittest.mock import Mock
from src.main.cores import Database
from mysql.connector import connect
from src.main.cores import ITable


class DatabaseTest(unittest.TestCase):
    host = "127.0.0.1"
    user = "root"
    password = "NnTeTo@Ml171002"
    database_name = 'testing_database'
    table_name = 'testing_table'

    def setUp(self):
        self.conn = connect(host=self.host, user=self.user, password=self.password)
        self.cursor = self.conn.cursor()
        self.database = Database(self.conn, self.database_name)

    def test_create_non_existed_database(self):

        self.cursor.execute("SHOW DATABASES")
        databases = self.cursor.fetchall()
        assert (self.database_name,) in databases

    def test_create_table(self):
        table = Mock(spec=ITable)
        table.get_create_query.return_value = f"CREATE TABLE {self.table_name} (id int)"
        
        self.database.create(table)

        self.cursor.execute("SHOW TABLES")
        tables = self.cursor.fetchall()
        assert (self.table_name,) in tables

    def tearDown(self):
        self.cursor.execute("DROP DATABASE testing_database")
