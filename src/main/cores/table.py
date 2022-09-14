from .i_table import ITable


class Table(ITable):
    def __init__(self, name="", columns=[]):
        self._name = name
        self._columns = columns

    def get_create_query(self):
        column_definitions = [column.get_definition() 
                    for column in self._columns]
        return f"CREATE TABLE {self._name} ({', '.join(column_definitions)})"
