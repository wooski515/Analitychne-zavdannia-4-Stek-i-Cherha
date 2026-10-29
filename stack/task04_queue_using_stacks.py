"""Стек, задача 4. Черга (FIFO) на двох стеках.

Зі стеками використовуються лише операції append (push to top),
pop() і [-1] (pop / peek from top) та перевірка на порожнечу.
"""


class MyQueue:
    def __init__(self):
        self.in_stack = []    # сюди додаються нові елементи
        self.out_stack = []   # звідси елементи забираються (у порядку черги)

    def push(self, x):
        self.in_stack.append(x)

    def _move(self):
        # Коли out_stack порожній, перекладаємо в нього всі елементи з in_stack:
        # порядок розвертається, і найстаріший елемент опиняється зверху
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self):
        self._move()
        return self.out_stack.pop()

    def peek(self):
        self._move()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack
