def gcd(a, b):
    if a == b:
        return a

    x = a
    y = b
    r = a % b

    while r != 0:
        x = y
        y = r
        r = x % y

    return y

a, b = list(map(int, input().split()))
result = gcd(a, b)
print(result)