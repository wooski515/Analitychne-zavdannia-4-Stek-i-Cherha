"""Стек, задача 3. Мінімальний стек: push, pop, top і getMin за O(1).

Разом з кожним елементом зберігаємо мінімум усього стека на момент додавання.
Тоді після pop мінімум автоматично "повертається" до попереднього значення.
"""


class MinStack:
    def __init__(self):
        self.stack = []   # пари (значення, мінімум стека з цим елементом)

    def push(self, val):
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
