class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # function to print out the linked list
    def node_print(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return ", ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.is_empty():
            self.head = node
            return
        nd = self.head
        while nd.next:
            nd = nd.next
        nd.next = node
        """
        for nd in self:
            pass
        nd.next = node
        """

    def remove_first(self):
        if self.is_empty():
            return "Empty list"
        self.head = self.head.next

    def remove_last(self):
        # if the list is empty, return Empty list
        if self.is_empty():
            return "Empty list"
        # if in the list there is only one node, return an empty list
        elif self.head.next is None:
            self.head = None
            return
        # else find the last node,
        # find the node before the last node nd_previous
        # and nd_previous node will be the last node by
        # assigning None to its pointer nd_previous.next = None
        else:
            nd_previous = self.head
            nd = nd_previous.next
            while nd.next:
                nd_previous = nd_previous.next
                nd = nd.next
            nd_previous.next = None

    # Function to find a node by its data in a list.
    # using this function when I insert a new node into the list
    # finds and returns the first node
    def find_node(self, node_data_to_find):
        if self.is_empty():
            return "Empty list"
        for node in self:
            if node.data == node_data_to_find:
                return node
        raise Exception("Node not found")

    # inserts a new node into the Linked list,
    def insert_node(self, node_data, new_data):
        try:
            node = self.find_node(node_data)
        except:
            print("Node not found")
            return
        new_node = Node(new_data)
        new_node.next = node.next
        node.next = new_node


llist = LinkedList()
first_node = Node("a")
llist.head = first_node
second_node = Node("b")
llist.add_last(second_node)
third_node = Node("c")
llist.add_last(third_node)
fourth_node = Node("d")
llist.add_last(fourth_node)
llist.remove_first()
llist.add_first(first_node)
fifth_node = Node("e")
llist.add_last(fifth_node)

print(llist.node_print())

llist.insert_node("e", "f")
llist.insert_node("f", "e")
print(llist.node_print())
"""
for node in llist:
    print(node.data)
"""