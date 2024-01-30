from AVL_tree import insert

sum = 0
def preorder_traversal_sum(root):
    if root:
        global sum 
        sum += root.key
        #print(root.key, sum)
        preorder_traversal_sum(root.left)
        preorder_traversal_sum(root.right)
    return f"Summa = {sum}"

if __name__ == "__main__":
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)
        print("Вставлено:", key)
        print("AVL-Дерево:")
        print(root)

    print(preorder_traversal_sum(root))