"""Черга: перевірка розв'язків на прикладах з умови та граничних випадках.

Запуск: python queue/test_queue.py
"""

import unittest

from operations import run_operations
from task01_first_unique_char import first_uniq_char
from task02_stack_using_queues import MyStack
from task03_recent_counter import RecentCounter
from task04_circular_deque import MyCircularDeque
from task05_circular_queue import MyCircularQueue
from task06_stamping_sequence import moves_to_stamp
from task07_sliding_window_max import max_sliding_window
from task08_constrained_subsequence_sum import constrained_subset_sum


def apply_stamps(stamp, length, moves):
    """Ставить штампи за списком ходів і повертає отриманий рядок."""
    s = ["?"] * length
    for i in moves:
        s[i:i + len(stamp)] = stamp
    return "".join(s)


class TestQueue(unittest.TestCase):
    def test_01_first_uniq_char(self):
        self.assertEqual(first_uniq_char("leopard"), 0)
        self.assertEqual(first_uniq_char("loveleopard"), 2)
        self.assertEqual(first_uniq_char("aabb"), -1)
        self.assertEqual(first_uniq_char("z"), 0)
        self.assertEqual(first_uniq_char("aabbc"), 4)

    def test_02_stack_using_queues(self):
        ops = ["MyStack", "push", "push", "top", "pop", "empty"]
        args = [[], [1], [2], [], [], []]
        self.assertEqual(run_operations(MyStack, ops, args), [None, None, None, 2, 2, False])
        ops = ["MyStack", "push", "push", "push", "pop", "pop", "top", "pop", "empty"]
        args = [[], [1], [2], [3], [], [], [], [], []]
        self.assertEqual(run_operations(MyStack, ops, args), [None, None, None, None, 3, 2, 1, 1, True])

    def test_03_recent_counter(self):
        ops = ["RecentCounter", "ping", "ping", "ping", "ping"]
        args = [[], [1], [100], [3001], [3002]]
        self.assertEqual(run_operations(RecentCounter, ops, args), [None, 1, 2, 3, 3])

    def test_04_circular_deque(self):
        ops = ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
               "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
        args = [[3], [1], [2], [3], [4], [], [], [], [4], []]
        self.assertEqual(run_operations(MyCircularDeque, ops, args),
                         [None, True, True, True, False, 2, True, True, True, 4])
        ops = ["MyCircularDeque", "getFront", "getRear", "deleteFront", "deleteLast", "isEmpty",
               "insertFront", "deleteLast", "isEmpty"]
        args = [[1], [], [], [], [], [], [7], [], []]
        self.assertEqual(run_operations(MyCircularDeque, ops, args),
                         [None, -1, -1, False, False, True, True, True, True])

    def test_05_circular_queue(self):
        ops = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue",
               "Rear", "isFull", "deQueue", "enQueue", "Rear"]
        args = [[3], [1], [2], [3], [4], [], [], [], [4], []]
        self.assertEqual(run_operations(MyCircularQueue, ops, args),
                         [None, True, True, True, False, 3, True, True, True, 4])
        ops = ["MyCircularQueue", "Front", "Rear", "deQueue", "isEmpty", "enQueue", "Front", "isFull"]
        args = [[1], [], [], [], [], [5], [], []]
        self.assertEqual(run_operations(MyCircularQueue, ops, args),
                         [None, -1, -1, False, True, True, 5, True])

    def test_06_stamping_sequence(self):
        # Правильних відповідей може бути кілька, тому перевіряємо сам результат штампування
        for stamp, target in (("abc", "ababc"), ("abca", "aabcaca"), ("ab", "abab"), ("a", "aaa")):
            moves = moves_to_stamp(stamp, target)
            self.assertTrue(moves)
            self.assertLessEqual(len(moves), 10 * len(target))
            self.assertEqual(apply_stamps(stamp, len(target), moves), target)
        self.assertEqual(moves_to_stamp("abc", "ababc"), [0, 2])
        self.assertEqual(moves_to_stamp("abc", "abd"), [])     # літери d у штампі немає
        self.assertEqual(moves_to_stamp("ab", "ba"), [])

    def test_07_max_sliding_window(self):
        self.assertEqual(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(max_sliding_window([1], 1), [1])
        self.assertEqual(max_sliding_window([9, 8, 7, 6], 2), [9, 8, 7])
        self.assertEqual(max_sliding_window([4, 2, 12, 3], 4), [12])

    def test_08_constrained_subset_sum(self):
        self.assertEqual(constrained_subset_sum([10, 2, -10, 5, 20], 2), 37)
        self.assertEqual(constrained_subset_sum([-1, -2, -3], 1), -1)
        self.assertEqual(constrained_subset_sum([10, -2, -10, -5, 20], 2), 23)
        self.assertEqual(constrained_subset_sum([5], 1), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
