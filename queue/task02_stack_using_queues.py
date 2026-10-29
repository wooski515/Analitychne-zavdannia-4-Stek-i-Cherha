"""Черга, задача 2. Стек (LIFO) на двох чергах.

deque використовується лише як звичайна черга: append (push to back),
popleft() і [0] (pop / peek from front), len() і перевірка на порожнечу.
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()   # елементи в порядку стека: верхівка - на початку черги
        self.q2 = deque()   # допоміжна черга

    def push(self, x):
        # Новий елемент ставимо першим у q2, за ним - усі старі елементи з q1
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return not self.q1
