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

def lcm(a, b):
    return (a * b) // gcd(a, b)


a, b = list(map(int, input().split()))
result = lcm(a, b)
print(result)