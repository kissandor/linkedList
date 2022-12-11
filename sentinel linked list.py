class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        sentinel = Node(None)
        self.head = self.tail = sentinel

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def is_empty(self):
        return self.head is self.tail

    def last_node(self):
        if self.is_empty():
            raise Exception("Node not found")
        node = self.head
        while node.next is not self.tail:
            node = node.next
        return node

    def add_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def remove_first(self):
        if self.is_empty():
            return "Empty list"
        self.head = self.head.next

    def add_last(self, data):
        if self.is_empty():
            self.add_first(data)
            return

        self.tail.data = data

        end_node = Node(None)
        self.tail.next = end_node
        self.tail = end_node

    def remove(self, node):
        if node is self.head:
            self.remove_first()
            return

        node.data = node.next.data
        node.next = node.next.next

        if node.next is None:
            self.tail = node
            return


llist = SLinkedList()
llist.add_last("a")
llist.add_last("b")
llist.add_last("c")

node = llist.last_node()
llist.remove(node)

for node in llist:
    print(node.data)