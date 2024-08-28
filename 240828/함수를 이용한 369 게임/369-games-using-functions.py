def sol(a, b):
    num = list(range(a, b + 1))
    target = [3, 6, 9]
    count = 0

    for n in num:
        if n % 3 == 0:
            count += 1
        elif (n // 10) in target or (n % 10) in target:
            count += 1
    
    return count

a, b = list(map(int, input().split()))
result = sol(a, b)
print(result)