from .singly_node import SinglyNode


class DoublyNode(SinglyNode):
    def __init__(self, value):
        super(DoublyNode, self).__init__(value)
        self.link_next: DoublyNode | None = None
        self.link_last: DoublyNode | None = None

    def append_tail(self, value) -> "DoublyNode":
        """
        Добавление значения в конец связного списка.
        :param value: Any
        :return: DoublyNode
        """

        link_current: DoublyNode = super().append_tail(value)
        link_current.link_next.link_last = link_current

        return link_current

