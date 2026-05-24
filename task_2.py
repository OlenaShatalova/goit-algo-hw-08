class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def sum_tree(root):
    """Знаходить суму всіх значень у BST.

    Алгоритм (postorder):
    1. Якщо вузол порожній — повертаємо 0
    2. Рахуємо суму лівого піддерева
    3. Рахуємо суму правого піддерева
    4. Повертаємо: ліва сума + права сума + значення поточного вузла
    """
    if root is None:
        return 0

    left_sum = sum_tree(root.left)
    right_sum = sum_tree(root.right)

    return left_sum + right_sum + root.val


# Тест
if __name__ == "__main__":
    root = Node(5)
    for val in [3, 2, 4, 7, 6, 8, 1]:
        root = insert(root, val)

    print("Дерево містить вузли: 5, 3, 2, 4, 7, 6, 8, 1")
    print(f"Сума всіх значень: {sum_tree(root)}")  # Очікується: 36