import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, max_size):
        self.top = None
        self.max_size = max_size
        self.current_size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return self.current_size == self.max_size

    def push(self, value):
        if not self.is_full():
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
            self.current_size += 1

    def to_list(self):
        values = []
        current = self.top
        while current:
            values.append(current.value)
            current = current.next
        for _ in range(self.max_size - len(values)):
            values.append("Empty")
        return values[::-1]  # Reverse to show bottom of the stack first


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def to_list_of_lists(self):
        return [stack.to_list() for stack in self]

