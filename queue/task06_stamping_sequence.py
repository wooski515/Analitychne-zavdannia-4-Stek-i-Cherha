"""Черга, задача 6. Штампування послідовності.

Ідея - йти "у зворотному напрямку": починаємо з target і шукаємо місце,
де можна "зняти" штамп, тобто де всі літери збігаються зі stamp
(символ "?" підходить до будь-якої літери). Знайдені літери замінюємо на "?".
Коли весь рядок став "?", ходи в зворотному порядку і є відповіддю:
останній знятий штамп ставився першим.
"""


def can_unstamp(s, stamp, i):
    """Чи можна зняти штамп з позиції i: літери збігаються, і є хоч одна не "?"."""
    has_letter = False
    for j in range(len(stamp)):
        if s[i + j] == "?":
            continue
        if s[i + j] != stamp[j]:
            return False
        has_letter = True
    return has_letter


def moves_to_stamp(stamp, target):
    """Повертає індекси штампування по ходах або [], якщо target отримати неможливо."""
    m, n = len(stamp), len(target)
    s = list(target)
    moves = []
    changed = True
    while changed:
        changed = False
        for i in range(n - m + 1):
            if can_unstamp(s, stamp, i):
                s[i:i + m] = ["?"] * m
                moves.append(i)
                changed = True
    # Кожен хід перетворює щонайменше одну літеру на "?", тому ходів не більше n <= 10 * n
    if all(ch == "?" for ch in s):
        return moves[::-1]
    return []
