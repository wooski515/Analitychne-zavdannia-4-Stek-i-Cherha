"""Черга, задача 8. Максимальна сума підпослідовності, де сусідні індекси відрізняються не більше ніж на k.

dp[i] - найбільша сума підпослідовності, що закінчується на nums[i]:
dp[i] = nums[i] + max(0, max(dp[i - k] ... dp[i - 1])).
Максимум у "вікні" з k попередніх dp шукаємо так само, як у задачі 7, -
двосторонньою чергою з індексами, значення dp за якими спадають. Складність O(n).
"""

from collections import deque


def constrained_subset_sum(nums, k):
    """Повертає максимальну суму непорожньої підпослідовності з умовою j - i <= k."""
    dp = [0] * len(nums)
    window = deque()
    for i, x in enumerate(nums):
        # Індекс вийшов за межі вікна з k попередніх елементів
        if window and window[0] < i - k:
            window.popleft()
        best_prev = dp[window[0]] if window else 0
        dp[i] = x + max(0, best_prev)   # від'ємну суму попередньої частини не беремо
        while window and dp[window[-1]] <= dp[i]:
            window.pop()
        window.append(i)
    return max(dp)
