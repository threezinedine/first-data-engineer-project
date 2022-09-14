import unittest
from unittest.mock import Mock
from src.main.cores import Table


class TableTest(unittest.TestCase):
    table_name = "testing_table"
    def setUp(self):
        self.table = Table(name=self.table_name, columns=[])

    def test_get_create_query_method(self):
        query = self.table.get_create_query()

        assert query == f"CREATE TABLE testing_table ()"

    def test_get_create_query_method_with_2_int_columns(self):
        pass

