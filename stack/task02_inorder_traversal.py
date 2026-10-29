"""Стек, задача 2. Обхід бінарного дерева в порядку (inorder): ліве - корінь - праве.

Замість рекурсії використовується явний стек.
"""


def inorder_traversal(root):
    """Повертає значення вузлів дерева в порядку inorder."""
    result = []
    stack = []
    node = root
    while node or stack:
        # Спускаємось ліворуч, запам'ятовуючи шлях у стеку
        while node:
            stack.append(node)
            node = node.left
        # Лівого піддерева більше немає - обробляємо вузол і йдемо праворуч
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result
