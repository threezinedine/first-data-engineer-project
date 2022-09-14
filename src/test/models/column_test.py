import unittest
from unittest.mock import Mock
from src.main.models import IntColumn


class ColumnTest(unittest.TestCase):
    def test_int_column_get_definition_method(self):
        id_column = IntColumn(name="id") 

        definition = id_column.get_definition()

        assert definition == "id int"
        
