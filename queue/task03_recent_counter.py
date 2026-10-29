"""Черга, задача 3. Кількість запитів за останні 3000 мс."""

from collections import deque


class RecentCounter:
    def __init__(self):
        self.requests = deque()   # моменти часу запитів у порядку зростання

    def ping(self, t):
        self.requests.append(t)
        # Запити, старші за t - 3000, вже ніколи не потраплять у вікно - видаляємо
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
