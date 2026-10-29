"""Стек: запуск усіх прикладів з умови.

Запуск: python stack/main.py
"""

import json

from operations import run_operations
from task01_valid_parentheses import is_valid
from task02_inorder_traversal import inorder_traversal
from task03_min_stack import MinStack
from task04_queue_using_stacks import MyQueue
from task05_decode_string import decode_string
from task06_eval_rpn import eval_rpn
from task07_longest_valid_parentheses import longest_valid_parentheses
from tree_node import build_tree


def show(value):
    """Друк у форматі умови: null, true, false."""
    return json.dumps(value)


print("1. Валідні дужки")
for s in ("()", "()[]{}", "(]"):
    print(f"  Input: s = {show(s)} -> Output: {show(is_valid(s))}")

print("\n2. Обхід бінарного дерева в порядку (Inorder Traversal)")
for values in ([1, None, 2, 3], [], [1]):
    print(f"  Input: root = {show(values)} -> Output: {show(inorder_traversal(build_tree(values)))}")

print("\n3. Мінімальний стек")
ops = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
args = [[], [-2], [0], [-3], [], [], [], []]
print(f"  Input: {show(ops)} {show(args)}")
print(f"  Output: {show(run_operations(MinStack, ops, args))}")

print("\n4. Черга на двох стеках")
ops = ["MyQueue", "push", "push", "peek", "pop", "empty"]
args = [[], [1], [2], [], [], []]
print(f"  Input: {show(ops)} {show(args)}")
print(f"  Output: {show(run_operations(MyQueue, ops, args))}")

print("\n5. Декодувати рядок")
for s in ("3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"):
    print(f"  Input: s = {show(s)} -> Output: {show(decode_string(s))}")

print("\n6. Зворотна польська нотація")
for tokens in (["2", "1", "+", "3", "*"],
               ["4", "13", "5", "/", "+"],
               ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]):
    print(f"  Input: tokens = {show(tokens)} -> Output: {eval_rpn(tokens)}")

print("\n7. Найдовші дійсні дужки")
for s in ("(()", ")()())", ""):
    print(f"  Input: s = {show(s)} -> Output: {longest_valid_parentheses(s)}")
