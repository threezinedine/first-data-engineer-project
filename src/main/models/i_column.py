from abc import ABC, abstractmethod


class IColumn(ABC):
    @abstractmethod
    def get_definition(self) -> str:
        pass
