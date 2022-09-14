from .i_table import ITable


class Table(ITable):
    def __init__(self, name="", columns=[]):
        pass

    def get_create_query(self):
        return "CREATE TABLE testing_table (id int)"
