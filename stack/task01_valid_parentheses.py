"""Стек, задача 1. Валідні дужки."""


def is_valid(s):
    """Повертає True, якщо всі дужки в s закриті правильно."""
    pairs = {")": "(", "]": "[", "}": "{"}   # закриваюча -> відповідна відкриваюча
    stack = []
    for ch in s:
        if ch in pairs:
            # Закриваюча дужка має відповідати останній відкритій
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    # Рядок дійсний, лише якщо не лишилось незакритих дужок
    return not stack
