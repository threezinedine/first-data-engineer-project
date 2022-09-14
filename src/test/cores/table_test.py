import unittest
from unittest.mock import Mock
from src.main.cores import Table


class TableTest(unittest.TestCase):
    def test_get_create_query_method(self):
        table = Table(name="testing_table", columns=[])

        query = table.get_create_query()

        assert query == f"CREATE TABLE testing_table ()"

    def test_get_create_query_method_with_2_int_columns(self):
        pass

