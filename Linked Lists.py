"""Implement an linked list class with some simple methods like inserting, deleting and traversing. 
Each of the elements of the linked list is given as an instance of a Node class, which can 
include a value and reference to the next node. insert method inserts nodes at the start, delete 
method deletes a node whose value is given. Traverse method provides the entire values of a 
linked list in form of a list. The example illustrates inserting, deleting and traversing 
the linked list.
"""

class Node:
    def __init__(self, value):
        # Initializing a node with a value and a next pointer set to None
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # Initializing an empty linked list
        self.head = None

    def insert(self, value):
        # Inserting a node at the beginning of the linked list
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        # Deleting a node with a specific value
        current = self.head
        if current is None:
            return
        if current.value == value:
            self.head = current.next
            return
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        # Traversing the linked list and returning all values
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements


# Example usage
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.delete(20)
print(linked_list.traverse()) 
