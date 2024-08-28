def gcd(a, b):
    r = a % b

    while True:
        x = b
        y = r
        r = x % y

        if r == 0:
            return y

a, b = list(map(int, input().split()))
result = gcd(a, b)
print(result)