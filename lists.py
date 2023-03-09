numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
strings.append("hello")
strings.append("world")
second_name = names[1]

for i in range(3):
    numbers.append(i+1)

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
