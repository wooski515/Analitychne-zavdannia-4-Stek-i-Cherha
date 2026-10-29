"""Черга: запуск усіх прикладів з умови.

Запуск: python queue/main.py
"""

import json

from operations import run_operations
from task01_first_unique_char import first_uniq_char
from task02_stack_using_queues import MyStack
from task03_recent_counter import RecentCounter
from task04_circular_deque import MyCircularDeque
from task05_circular_queue import MyCircularQueue
from task06_stamping_sequence import moves_to_stamp
from task07_sliding_window_max import max_sliding_window
from task08_constrained_subsequence_sum import constrained_subset_sum


def show(value):
    """Друк у форматі умови: null, true, false."""
    return json.dumps(value)


def print_operations(cls, ops, args):
    print(f"  Input: {show(ops)} {show(args)}")
    print(f"  Output: {show(run_operations(cls, ops, args))}")


print("1. Перший унікальний символ у рядку")
for s in ("leopard", "loveleopard", "aabb"):
    print(f"  Input: s = {show(s)} -> Output: {first_uniq_char(s)}")

print("\n2. Стек на двох чергах")
print_operations(MyStack,
                 ["MyStack", "push", "push", "top", "pop", "empty"],
                 [[], [1], [2], [], [], []])

print("\n3. Кількість останніх викликів")
print_operations(RecentCounter,
                 ["RecentCounter", "ping", "ping", "ping", "ping"],
                 [[], [1], [100], [3001], [3002]])

print("\n4. Замкнута двобічна черга (Deque)")
print_operations(MyCircularDeque,
                 ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
                  "getRear", "isFull", "deleteLast", "insertFront", "getFront"],
                 [[3], [1], [2], [3], [4], [], [], [], [4], []])

print("\n5. Замкнута черга")
print_operations(MyCircularQueue,
                 ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue",
                  "Rear", "isFull", "deQueue", "enQueue", "Rear"],
                 [[3], [1], [2], [3], [4], [], [], [], [4], []])

print("\n6. Штампування послідовності")
for stamp, target in (("abc", "ababc"), ("abca", "aabcaca")):
    moves = moves_to_stamp(stamp, target)
    print(f"  Input: stamp = {show(stamp)}, target = {show(target)} -> Output: {moves}")
    s = ["?"] * len(target)
    for i in moves:   # показуємо, як рядок змінюється після кожного ходу
        s[i:i + len(stamp)] = stamp
        print(f"    штамп в індекс {i}: {''.join(s)}")

print("\n7. Максимум плаваючого вікна")
for nums, k in (([1, 3, -1, -3, 5, 3, 6, 7], 3), ([1], 1)):
    print(f"  Input: nums = {nums}, k = {k} -> Output: {max_sliding_window(nums, k)}")

print("\n8. Обмежена сума підпослідовності")
for nums, k in (([10, 2, -10, 5, 20], 2), ([-1, -2, -3], 1), ([10, -2, -10, -5, 20], 2)):
    print(f"  Input: nums = {nums}, k = {k} -> Output: {constrained_subset_sum(nums, k)}")
