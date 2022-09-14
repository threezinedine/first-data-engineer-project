import unittest
from unittest.mock import Mock
from src.main.cores import Table


class TableTest(unittest.TestCase):
    def test_get_create_query_method(self):
        id_column = Mock()
        table = Table(name="testing_table", columns=[
                id_column                 
            ])

        query = table.get_create_query()

        assert query == f"CREATE TABLE testing_table (id int)"
