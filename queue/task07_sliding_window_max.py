"""Черга, задача 7. Максимум у ковзному вікні розміру k.

Двостороння черга зберігає індекси, значення за якими спадають.
На початку черги завжди максимум поточного вікна. Складність O(n).
"""

from collections import deque


def max_sliding_window(nums, k):
    """Повертає список максимумів для кожного положення вікна."""
    window = deque()
    result = []
    for i, x in enumerate(nums):
        # Індекс на початку черги вийшов за межі вікна
        if window and window[0] <= i - k:
            window.popleft()
        # Менші за x елементи вже ніколи не стануть максимумом
        while window and nums[window[-1]] <= x:
            window.pop()
        window.append(i)
        if i >= k - 1:   # вікно вже повністю сформоване
            result.append(nums[window[0]])
    return result
