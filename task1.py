from AVL_tree import insert

def max_value_node(node):
    current = node
    while current.right is not None:
        current = current.right
    return f"max value = {current.key}"

if __name__ == "__main__":
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)
        print("Вставлено:", key)
        print("AVL-Дерево:")
        print(root)

    print(max_value_node(root))