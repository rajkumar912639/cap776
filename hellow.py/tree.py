# Create the root node
root = Node("A")
# Create the first level children
root.add_child(Node("B"))
root.add_child(Node("C"))
root.add_child(Node("D"))
# Create the second level children
root.children[0].add_child(Node("E"))
root.children[0].add_child(Node("F"))
root.children[2].add_child(Node("G"))
root.children[2].add_child(Node("H"))
# Print the tree
root.print_tree()
