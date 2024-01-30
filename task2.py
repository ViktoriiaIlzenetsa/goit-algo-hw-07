from AVL_tree import insert

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return f"min value = {current.key}"

if __name__ == "__main__":
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)
        print("Вставлено:", key)
        print("AVL-Дерево:")
        print(root)

    print(min_value_node(root))