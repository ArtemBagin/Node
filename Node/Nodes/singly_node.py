from .abcnode import ABCNode


class SinglyNode(ABCNode):
    def __init__(self, value):
        self.value = value
        self.link_next: SinglyNode | None = None

    def append_tail(self, value) -> "SinglyNode":
        """
        Добавление значения в конец связного списка.
        :param value: Any
        :return: object Node
        """

        link_current = self

        while link_current.link_next:
            link_current = link_current.link_next

        link_current.link_next = SinglyNode(value=value)
        return link_current

    def append_begin(self, value):
        """
        Добавление значения в начало связного списка.
        :param value: Any
        :return: None
        """

        node = SinglyNode(value=value)

        for val in self.values:
            node.append_tail(val)

        self.__dict__ = node.__dict__
        del node  # для контроля памяти

    def append_after(self, after_value, value):
        """
        Добавление элемента после заданого
        :param after_value: Any
        :param value: Any
        :return: None
        """

        node = SinglyNode(0)
        for val in self.values:
            if val == after_value:
                node.append_tail(val)
                node.append_tail(value)
            else:
                node.append_tail(val)

        node.remove_begin()
        self.__dict__ = node.__dict__
        del node  # для контроля памяти

    def find(self, value):
        """
        Возращает номер элемента по значению
        :param value: Any
        :return: int
        """

        c = 0
        for val in self.values:
            if val == value:
                return c
            c += 1
        return -1

    def remove(self, value):
        """
        Удаления элемента по значению
        :param value: int
        :return: None
        """

        link_current = self

        if link_current.value == value:
            self.remove_begin()
            return

        while link_current.link_next:
            if not (link_current.link_next.value == value):
                link_current = link_current.link_next
            else:
                link_current.link_next = link_current.link_next.link_next

    def remove_begin(self):
        """
        Удаления элемента с начала списка
        :return: None
        """

        node = SinglyNode(self.link_next.value)
        link_current = self.link_next

        while link_current.link_next:
            node.append_tail(link_current.link_next.value)
            link_current = link_current.link_next

        self.__dict__ = node.__dict__
        del node  # для контроля памяти

    def remove_tail(self):
        """
        Удаление элемента с конца списка
        :return: None
        """

        link_current = self

        while link_current.link_next:
            last = link_current
            link_current = link_current.link_next

        link_current = last
        link_current.link_next = None

    @property
    def values(self):
        """
        Генератор элементов связого списка.
        :return: generator object Node.get_values
        """

        link_current = self

        yield link_current.value
        while link_current.link_next:
            link_current = link_current.link_next
            yield link_current.value

