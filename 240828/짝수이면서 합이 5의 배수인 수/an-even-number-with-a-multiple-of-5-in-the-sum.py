def sol(n):
    return not(n % 2 and ((n // 10) + (n % 10)) % 5)

n = int(input())

if (sol(n)):
    print("Yes")
else:
    print("No")