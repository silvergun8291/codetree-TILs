def print_rectangle(n: int) -> None:
    num = list(range(1, 10))

    for i in range(n * n):
        print(num[i % 9], end=' ')

        if (i + 1) % 4 == 0:
            print()

n = int(input())
print_rectangle(n)