def run(x, a, b, i, j):
    k = j
    ct = 0
    while k > i-1:
        if x[k] <= b and not (x[k] <= a):
            ct = ct + 1
        k = k -1
    return ct

x = [11, 10, 10, 5, 10, 15, 20, 10, 7, 11]
a = run(x, 8, 18, 3, 6)

print(a)