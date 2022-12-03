from abc import ABC, abstractmethod
from typing import NoReturn, Iterable, Any


class ABCNode(ABC):
    """Abstract Node class"""

    @abstractmethod
    def append_tail(self, value: Any) -> NoReturn:
        pass

    @abstractmethod
    def append_begin(self, value: Any) -> NoReturn:
        pass

    @abstractmethod
    def append_after(self, after_value: Any, value: Any) -> NoReturn:
        pass

    @abstractmethod
    def values(self) -> Iterable[int]:
        yield int

    @abstractmethod
    def find(self, value: Any) -> int:
        pass

    @abstractmethod
    def remove_tail(self) -> NoReturn:
        pass

    @abstractmethod
    def remove_begin(self) -> NoReturn:
        pass

    @abstractmethod
    def remove(self, value: int) -> int:
        pass

