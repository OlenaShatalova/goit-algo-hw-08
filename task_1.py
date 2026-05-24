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


def find_min(root):
    """Знаходить найменше значення у BST.

    Алгоритм:
    1. Якщо дерево порожнє — повертаємо None
    2. Йдемо вліво доки є лівий нащадок
    3. Останній вузол без лівого нащадка — це мінімум
    """
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current.val


# Тест
if __name__ == "__main__":
    root = Node(5)
    for val in [3, 2, 4, 7, 6, 8, 1]:
        root = insert(root, val)

    print("Дерево містить вузли: 5, 3, 2, 4, 7, 6, 8, 1")
    print(f"Найменше значення: {find_min(root)}")  # Очікується: 1