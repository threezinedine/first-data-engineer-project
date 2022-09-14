from abc import ABC, abstractmethod


class ITable(ABC):
    @abstractmethod
    def get_create_query(self) -> str:
        pass
