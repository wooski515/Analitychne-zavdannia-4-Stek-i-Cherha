"""Черга, задача 5. Циклічна черга ("кільцевий буфер") розміру k.

Вбудовані черги не використовуються: дані лежать у звичайному масиві
довжини k, а індекси "загортаються" через % k.
"""


class MyCircularQueue:
    def __init__(self, k):
        self.data = [0] * k
        self.capacity = k
        self.head = 0   # індекс першого елемента
        self.size = 0   # кількість елементів у черзі

    def enQueue(self, value):
        if self.isFull():
            return False
        self.data[(self.head + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.data[self.head]

    def Rear(self):
        return -1 if self.isEmpty() else self.data[(self.head + self.size - 1) % self.capacity]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
