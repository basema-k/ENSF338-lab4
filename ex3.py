import sys
import timeit

# 1:
# When arrays are full, 

# 2:
mylist = []
prev_size = sys.getsizeof(mylist)

for n in range(64):
    mylist.append(n)
    new_size = sys.getsizeof(mylist)

    if new_size != prev_size:
        print("Capcity changed: ", new_size, "bytes")
        prev_size = new_size

# 3:
slist = []






