def print_rectangle(n: int, m: int) -> None:
    for _ in range(n):
        for _ in range(m):
            print('1', end="")
        print()

n, m = list(map(int, input().split()))
print_rectangle(n, m)