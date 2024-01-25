class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(node, key):
    if node is None:
        return Node(key)
    else:
        if key < node.val:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
    return node


def get_max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val


def get_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val


def get_sum_of_values(node):
    if node is None:
        return 0
    return node.val + get_sum_of_values(node.left) + get_sum_of_values(node.right)


root = Node(5)
insert(root, 10)
insert(root, 2)
insert(root, 13)
insert(root, 45)
insert(root, 5)

max_value = get_max_value(root)
print("Найбільше значення:", max_value)

min_value = get_min_value(root)
print("Найменше значення:", min_value)

sum = get_sum_of_values(root)
print("Сума:", sum)
