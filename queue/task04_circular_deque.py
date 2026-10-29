"""Черга, задача 4. Циклічна двостороння черга (deque) фіксованого розміру k.

Елементи зберігаються у звичайному масиві довжини k. front - індекс першого
елемента, size - кількість елементів. Індекси "загортаються" через % k,
тому кінець масиву з'єднується з початком.
"""


class MyCircularDeque:
    def __init__(self, k):
        self.data = [0] * k
        self.capacity = k
        self.front = 0
        self.size = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity   # крок назад по колу
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.data[(self.front + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self):
        return -1 if self.isEmpty() else self.data[self.front]

    def getRear(self):
        return -1 if self.isEmpty() else self.data[(self.front + self.size - 1) % self.capacity]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
