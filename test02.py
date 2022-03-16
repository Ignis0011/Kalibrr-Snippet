def h(n, strings):
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        strings = f(strings)
    return strings

def f(strings):
    if len(strings) == 0:
        return ""
    elif len(strings) == 1:
        return strings
    else:
        return f(g(strings)) + strings[0]

def g(strings):
    i = 0
    new_str = ""
    while i < (len(strings) - 1):
        new_str = new_str + strings[i + 1]
        i = i + 1
    return new_str

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

print(h(1, "fruits"))
print(h(2, "fruits"))
print(h(5, "fruits"))
#print(h(power(2, 1000000000000000), "fruits"))
#print(h(power(2, 9831050005000007), "fruits"))