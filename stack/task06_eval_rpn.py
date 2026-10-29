"""Стек, задача 6. Обчислити вираз у зворотній польській нотації."""


def eval_rpn(tokens):
    """Повертає значення виразу, наприклад ["2", "1", "+", "3", "*"] -> 9."""
    stack = []
    for token in tokens:
        if token in ("+", "-", "*", "/"):
            b = stack.pop()   # правий операнд лежить зверху
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))   # ділення з відкиданням дробової частини (до нуля)
        else:
            stack.append(int(token))
    return stack[0]
