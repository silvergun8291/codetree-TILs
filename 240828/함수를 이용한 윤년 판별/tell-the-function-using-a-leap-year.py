def solve(year):
    if year == 0:
        return False
    
    if year % 4 == 0 and not(year % 100 == 0 and year % 400 != 0):
        return True
    else:
        return False

a = int(input())
result = solve(a)
print(result)