def sol(a, b, c):
    return min(a, b, c)

a, b, c = list(map(int, input().split()))
result = sol(a, b, c)
print(result)