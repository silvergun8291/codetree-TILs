def sol(n):
    return n % 2 == 0 and ((n // 10) + (n % 10)) % 5 == 0

n = int(input())

if (sol(n)):
    print("Yes")
else:
    print("No")