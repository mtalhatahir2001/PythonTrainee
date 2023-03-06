a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

c = a.difference(a.intersection(b))
print(c)
