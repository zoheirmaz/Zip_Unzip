from Node import Node


def tree(node2, node1):
    node = Node(node1.index + node2.index)
    if node1 < node2:
        node.left = node1
        node.right = node2
    else:
        node.left = node2
        node.right = node1
    return node


def read():
    None


def write():
    None


