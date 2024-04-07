# тест

def is_possible(n, x, y, mid):
    return (mid // x) + (mid // y) >= n

def min_time_to_copy(n, x, y):
    left, right = 0, n * min(x, y)

    while left < right:
        mid = (left + right) // 2
        if is_possible(n, x, y, mid):
            right = mid
        else:
            left = mid + 1

    return left

n, x, y = map(int, input().split())

print(min_time_to_copy(n, x, y))