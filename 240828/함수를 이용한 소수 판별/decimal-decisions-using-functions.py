def solve(a, b):
    num = list(range(a, b + 1))
    prime = []

    for k in num:
        if is_prime(k):
            prime.append(k)

    return sum(prime)

def is_prime(k):
    for i in range(2, k):
        if k % i == 0:
            return False

    return True


a, b = list(map(int, input().split()))
result = solve(a, b)
print(result)