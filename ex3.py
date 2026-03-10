import sys
import timeit
import matplotlib.pyplot as plt

# Exercise 3 - Lab 4

# 1:
# Python grows lists in the function list_resize
# line 44: list_resize(PyListObject *self, Py_ssize_t newsize)

# line 70: new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;
# line 70 is the line which determines how much extra space (capacity) to allocate when a list grows
# the comment above the formula tells us that the over-allocation prevents Python from having to resize on every append

# growth factor:
# new_allocated = newsize + (newsize >> 3) + 6
# newsize >> 3 is shift right by 3 bits, which is the same newsize/8 -> 1/8 of newsize
# so newsize/8 is added as extra space on every append
# so then the growth factor is (1/8 = 12.5%)

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
S = 1000
slist = list(range(S))

t1 = timeit.timeit(
    stmt = "slist.append(0)",
    setup="S=1000; slist = list(range(S))",
    number = 1000)
print("Average time (S -> S+1):", t1/1000)

# 4:
t2 = timeit.timeit(
    stmt="slist.append(0)",
    setup="S=1000; slist = list(range(S-1))",
    number = 1000)
print("Average time (S-1 -> S):", t2/1000)

# 5:

# S -> S+1
timer1 = timeit.Timer(
    stmt = "slist.append(0)",
    setup = "S=1000; slist = list(range(S))"
)
# S-1 -> S
timer2 = timeit.Timer(
    stmt = "slist.append(0)",
    setup = "S=1000; slist = list(range(S-1))"
)
# collect 1000 individual measurements
# perform 1 append, 1000 separate times
times1 = timer1.repeat(repeat=1000, number=1)
times2 = timer2.repeat(repeat=1000, number=1)

plt.hist(times1, bins=30, alpha=0.6, label="S -> S+1")
plt.hist(times2, bins=30, alpha=0.6, label="S-1 -> S")

plt.xlabel("Time per append (seconds)")
plt.ylabel("Frequency")
plt.title("Distribution of Append Times")
plt.legend()
plt.xlim(0, 0.000009) # change x axis to better fit data
plt.show()

# 5 : Differences in plots
# Both cases are fast most of the time, so the histograms look pretty similar.
# The key difference is that S->S+1 has a few rare slow outliers
# Those are the moments when Python realizes the list is full and has to allocate new memory.
# S−1->S has no such outliers because the list always has one spare slot ready, so it just drops the element in 
