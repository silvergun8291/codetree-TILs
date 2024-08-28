def sol(n):
    return sum(list(range(1, n + 1))) // 10

n = int(input())
result = sol(n)
print(result)