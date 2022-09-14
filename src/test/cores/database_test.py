import unittest 
from src.main.cores import Database
from mysql.connector import connect


class DatabaseTest(unittest.TestCase):
    host = "127.0.0.1"
    user = "root"
    password = "NnTeTo@Ml171002"

    def setUp(self):
        self.conn = connect(host=self.host, user=self.user, password=self.password)
        self.cursor = self.conn.cursor()

    def test_create_non_existed_database(self):
        database = Database(self.conn, 'testing_database')

        self.cursor.execute("SHOW DATABASES")
        databases = self.cursor.fetchall()

        assert ('testing_database',) in databases

    def tearDown(self):
        self.cursor.execute("DROP DATABASE testing_database")
