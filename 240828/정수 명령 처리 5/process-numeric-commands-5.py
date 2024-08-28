codes = []
stack = []

n = int(input())

for _ in range(n):
    code = input()
    codes.append(code)

for code in codes:
    if len(code.split()) == 1:
        if code == 'pop_back':
            stack.pop()
        elif code == 'size':
            print(len(stack))
    else:
        instruction, value = code.split()

        if instruction == 'push_back':
            stack.append(value)
        elif instruction == 'get':
            print(stack[int(value) - 1])