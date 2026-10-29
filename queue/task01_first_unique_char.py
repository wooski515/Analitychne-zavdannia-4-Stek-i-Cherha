"""Черга, задача 1. Перший неповторюваний символ у рядку.

У черзі зберігаємо кандидатів (символ, індекс) у порядку появи.
Якщо символ на початку черги вже повторився, він більше не кандидат -
виймаємо його. Тоді на початку черги завжди перший унікальний символ.
"""

from collections import deque


def first_uniq_char(s):
    """Повертає індекс першого символу, що зустрічається один раз, або -1."""
    counts = {}
    candidates = deque()
    for i, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        candidates.append((ch, i))
        while candidates and counts[candidates[0][0]] > 1:
            candidates.popleft()
    return candidates[0][1] if candidates else -1
