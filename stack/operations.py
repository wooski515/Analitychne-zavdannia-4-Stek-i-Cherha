"""Виконання послідовності операцій над класом у форматі умови:
["MinStack", "push", "getMin"], [[], [-2], []] -> [None, None, -2].
"""


def run_operations(cls, operations, arguments):
    """Створює об'єкт класу cls і по черзі викликає його методи, повертає результати."""
    obj = cls(*arguments[0])
    outputs = [None]   # конструктор нічого не повертає
    for name, args in zip(operations[1:], arguments[1:]):
        outputs.append(getattr(obj, name)(*args))
    return outputs
