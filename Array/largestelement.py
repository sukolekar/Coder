ar = [6,4,3,6,99,8,89]
sorAr = sorted(ar)
getlast = sorAr.pop()
print("Largest element in the array: ", getlast)

import sys
sys.exit(0)
large = 0
for i in range(5,50):
    if i > large:
        large = i
print(large)