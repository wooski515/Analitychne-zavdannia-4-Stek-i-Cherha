"""Стек, задача 5. Декодувати рядок виду k[encoded_string]."""


def decode_string(s):
    """Повертає декодований рядок, наприклад "3[a2[c]]" -> "accaccacc"."""
    stack = []      # пари (рядок перед "[", кількість повторень)
    current = ""    # рядок, що збирається всередині поточних дужок
    num = 0         # число перед "[" (може бути багатоцифровим)
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            # Відкладаємо вже зібране і починаємо збирати вміст дужок
            stack.append((current, num))
            current, num = "", 0
        elif ch == "]":
            prev, k = stack.pop()
            current = prev + current * k
        else:
            current += ch
    return current
