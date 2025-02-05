
import sys


# print(sys.argv)

data = sys.argv

print(data)

# print(data[1] + data[2])

# print(data[1] + data[2])

# Python program to demonstrate
# sys.argv

# for i in data[1]:
#     # p = data[i]
#     print(i)

import sys

total = 0

for i in range(0,len(data)):
    if i != 0:
        total += int(data[i])
print(total)
 
