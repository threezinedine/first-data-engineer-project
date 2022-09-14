import unittest
from unittest.mock import Mock
from src.main.cores import Table
from src.main.models import IColumn


class TableTest(unittest.TestCase):
    table_name = "testing_table"
    def setUp(self):
        pass

    def test_get_create_query_method_without_attribute(self):
        self.table = Table(name=self.table_name, columns=[])

        query = self.table.get_create_query()

        assert query == f"CREATE TABLE testing_table ()"

    def test_get_create_query_method_with_id_int_columns(self):
        id_column = Mock(spec=IColumn)
        id_column.get_definition.return_value = "id int"

        self.table = Table(name=self.table_name, columns=[
                id_column
            ])

        query = self.table.get_create_query()

        assert query == f"CREATE TABLE testing_table (id int)"


    def test_get_create_query_method_with_id_int_columns(self):
        id_column = Mock(spec=IColumn)
        id_column.get_definition.return_value = "id int"
        name_column = Mock(spec=IColumn) 
        name_column.get_definition.return_value = "name varchar(23)"

        self.table = Table(name=self.table_name, columns=[
                id_column, name_column
            ])

        query = self.table.get_create_query()

        assert query == f"CREATE TABLE testing_table (id int, name varchar(23))"
