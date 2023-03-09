l = [2,4,7,3,14,19]
for i in l:
    is_odd = lambda x: (x % 2) != 0
    print(is_odd(i))
    