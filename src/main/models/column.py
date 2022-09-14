from .i_column import IColumn
from abc import abstractmethod


class Column(IColumn):
    def __init__(self, name=""):
        self._name = name

    @abstractmethod
    def _get_type(self) -> str:
        pass

    def get_definition(self) -> str:
        return f"{self._name} {self._get_type()}"


class IntColumn(Column):
    def __init__(self, name=""):
        super().__init__(name)

    def _get_type(self) -> str:
        return "int"
