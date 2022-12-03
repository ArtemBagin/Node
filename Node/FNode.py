from .Nodes import *


class Node:
    @staticmethod
    def SinglyNode(value):
        return singly_node.SinglyNode(value)

    @staticmethod
    def DoublyNode(value):
        return doubly_node.DoublyNode(value)


    @staticmethod
    def CyclicalNode(value):
        return cyclica_node.CyclicalNode(value)

