"""Defining a TreeNode class to represent each node in a rooted tree, where each node contains 
a value and a list of children. The add_child method allows adding child nodes, while the 
remove_child method removes a specific child by value. The display method recursively prints 
the tree structure with indentation to visually represent the hierarchy of nodes. The example 
usage constructs a tree with a root node and several child nodes, then displays the tree's structure.
"""

class TreeNode:
    def __init__(self, value):
        # Initializing the node with a value and an empty list for children
        self.value = value
        self.children = []

    def add_child(self, child_node):
        # Adding a child node to the list of children
        self.children.append(child_node)

    def remove_child(self, child_value):
        # Removing a child node by value
        for child in self.children:
            if child.value == child_value:
                self.children.remove(child)
                return

    def display(self, level=0):
        # Displaying the tree structure 
        print(' ' * level * 2 + str(self.value))
        for child in self.children:
            child.display(level + 1)

# Example usage
root = TreeNode(1)  
child1 = TreeNode(2)  
child2 = TreeNode(3)
child3 = TreeNode(4)

# Adding children to the root node
root.add_child(child1)  
root.add_child(child2)
root.add_child(child3)

# Adding a child to child1
child1.add_child(TreeNode(5))  
child1.add_child(TreeNode(6))

# Adding a child to child2
child2.add_child(TreeNode(7))  

 # Displaying the tree structure
root.display() 
