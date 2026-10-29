"""Стек: перевірка розв'язків на прикладах з умови та граничних випадках.

Запуск: python stack/test_stack.py
"""

import unittest

from operations import run_operations
from task01_valid_parentheses import is_valid
from task02_inorder_traversal import inorder_traversal
from task03_min_stack import MinStack
from task04_queue_using_stacks import MyQueue
from task05_decode_string import decode_string
from task06_eval_rpn import eval_rpn
from task07_longest_valid_parentheses import longest_valid_parentheses
from tree_node import build_tree


class TestStack(unittest.TestCase):
    def test_01_valid_parentheses(self):
        self.assertTrue(is_valid("()"))
        self.assertTrue(is_valid("()[]{}"))
        self.assertFalse(is_valid("(]"))
        self.assertTrue(is_valid("{[()]}"))
        self.assertFalse(is_valid("([)]"))
        self.assertFalse(is_valid("("))
        self.assertFalse(is_valid("]"))

    def test_02_inorder_traversal(self):
        self.assertEqual(inorder_traversal(build_tree([1, None, 2, 3])), [1, 3, 2])
        self.assertEqual(inorder_traversal(build_tree([])), [])
        self.assertEqual(inorder_traversal(build_tree([1])), [1])
        self.assertEqual(inorder_traversal(build_tree([4, 2, 6, 1, 3, 5, 7])), [1, 2, 3, 4, 5, 6, 7])

    def test_03_min_stack(self):
        ops = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
        args = [[], [-2], [0], [-3], [], [], [], []]
        self.assertEqual(run_operations(MinStack, ops, args), [None, None, None, None, -3, None, 0, -2])
        # Однакові мінімуми: після pop одного з них мінімум лишається
        ops = ["MinStack", "push", "push", "push", "pop", "getMin"]
        args = [[], [1], [0], [0], [], []]
        self.assertEqual(run_operations(MinStack, ops, args), [None, None, None, None, None, 0])

    def test_04_queue_using_stacks(self):
        ops = ["MyQueue", "push", "push", "peek", "pop", "empty"]
        args = [[], [1], [2], [], [], []]
        self.assertEqual(run_operations(MyQueue, ops, args), [None, None, None, 1, 1, False])
        ops = ["MyQueue", "push", "push", "pop", "push", "pop", "pop", "empty"]
        args = [[], [1], [2], [], [3], [], [], []]
        self.assertEqual(run_operations(MyQueue, ops, args), [None, None, None, 1, None, 2, 3, True])

    def test_05_decode_string(self):
        self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")
        self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")
        self.assertEqual(decode_string("10[a]"), "a" * 10)   # багатоцифрове число

    def test_06_eval_rpn(self):
        self.assertEqual(eval_rpn(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(eval_rpn(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)
        self.assertEqual(eval_rpn(["-7", "2", "/"]), -3)   # ділення до нуля, а не до -4

    def test_07_longest_valid_parentheses(self):
        self.assertEqual(longest_valid_parentheses("(()"), 2)
        self.assertEqual(longest_valid_parentheses(")()())"), 4)
        self.assertEqual(longest_valid_parentheses(""), 0)
        self.assertEqual(longest_valid_parentheses("()(())"), 6)
        self.assertEqual(longest_valid_parentheses("))(("), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
