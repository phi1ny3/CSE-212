class BST:
    # Nodes are a part of BSTs, so they should be part of the larger class
    class Node:
        def __init__(self,data):
            self.left = None
            self.right = None
            self.data = data

    def insert(self, data):
	    if self.root is None:
            # Make the new root
		    self.root = BST.Node(data)
	    else:
            # Call recursively to start at the root
		    self._insert(data, self.root)

    def __init__(self):
        self.root = None

    def _insert(self, data, node):
        if data < node.data:
            # Move to the left
            if node.left is None:
                # empty spot
                node.left = BST.Node(data)
            else:
                # If the value belongs in the left but still hasn't found an empty node, keep going
                # Calls itself recursively to keep going left
                self._insert(data, node.left)
        elif data >= node.data:
            # Move to the right
            if node.right is None:
                # empty spot
                node.right = BST.Node(data)
            else:
                # If the value belongs in the right but still hasn't found an empty node, keep going
                # Calls itself recursively to keep going right
                self._insert(data, node.right)

    def __iter__(self):
        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
    
    def _traverse_backward(self, node):
        # proceeding only if node is not None
        if node is not None:
            # yielding from right subtree first
            yield from self._traverse_backward(node.right)
            # then yielding this node's data
            yield node.data
            # yielding from left subtree
            yield from self._traverse_backward(node.left)

    def __reversed__(self):
        yield from self._traverse_backward(self.root)



val1 = input("What is the first item you want to insert? ")
val2 = input("What is the second item you want to insert? ")
val3 = input("What is the third item you want to insert? ")
val4 = input("What is the fourth item you want to insert? ")
val5 = input("What is the fifth item you want to insert? ")

tree = BST()
tree.insert(val1)
tree.insert(val2)
tree.insert(val3)
tree.insert(val4)
tree.insert(val5)

print("Here is the tree traversed forward: ")
for x in (tree):
    print(x)

valf = input("What value are you looking for? ")
print(valf in tree)

print("Here is the tree reversed: ")
for x in reversed(tree):
    print(x)