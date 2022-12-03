from .doubly_node import DoublyNode
from typing import NoReturn


class CyclicalNode(DoublyNode):
    def __init__(self, value):
        self.value = value
        self.link_next: CyclicalNode | None = None
        self.link_first: CyclicalNode = self
        self.link_last: CyclicalNode | None = None
        self.is_last: bool = False

        if not self.link_last:
            self.link_first = self

        if self.is_last:
            self.link_next = self.link_first
        else:
            self.link_next = self.link_next

    def append_tail(self, value) -> NoReturn:
        """
        Добавление значения в конец связного списка.
        :param value: Any
        :return: None
        """

        link_current = self

        while link_current.link_next:
            link_current = link_current.link_next

        link_current.link_next = CyclicalNode(value=value)
        link_current.is_last = False
        link_current.link_next.link_next = link_current.link_first
        link_current.link_next.is_last = True


    @property
    def values(self):
        """
        Генератор элементов связого списка.
        :return: generator object Node.get_values
        """

        link_current = self

        yield link_current.value
        while not link_current.is_last:
            link_current = link_current.link_next
            yield link_current.value

