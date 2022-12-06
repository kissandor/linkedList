class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "--> ".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

#not working yet
    def add_last(self, node):
        if self.head is None:
            self.head = node
        nd = self.head
        while nd is not None:
            nd = nd.next
        nd.next = node

    def remove_first(self):
        if self.head is None:
            return "Empty list"
        self.head = self.head.next


llist = LinkedList()
first_node = Node("a")
llist.head = first_node
second_node = Node("b")
first_node.next = second_node
third_node = Node("c")
second_node.next = third_node
fourth_node = Node("d")
third_node.next = fourth_node
print(llist)
llist.remove_first()
print(llist)
fith_node = Node("e")
llist.add_first(first_node)
print(llist)