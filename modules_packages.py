import re

# Your code goes here
find_members = []

for i in re.__all__:
    if i.find("find") != -1:
        find_members.append(i)

find_members.sort()
print(find_members)