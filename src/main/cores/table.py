from .i_table import ITable


class Table(ITable):
    def __init__(self, name="", columns=[]):
        self._name = name
        self._columns = columns

    def get_create_query(self):
        return f"CREATE TABLE {self._name} (id int)"
