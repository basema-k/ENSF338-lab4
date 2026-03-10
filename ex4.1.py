def processdata(li): # complexity analysis
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

# 1:
# Lets say n = len(li)
# The outer loop always runs n times
# The inner loop runs n times, but only when li[i] > 5.

# Worst Case: O(n^2)
# Every element is > 5, so the inner loop runs for every i.
# Example input: [6, 7, 8, 9, ...]

# Best Case: O(n)
# No element is > 5, so the inner loop never runs.
# Only the outer loop executes: n iterations.
# Example input: [1, 2, 3, 4, ...]

# Average Case: O(n^2)
# On a random input, some constant fraction of elements will be > 5.
# Lets say half the elements trigger the inner loop: (n/2) * n = n^2/2 = O(n^2).
# As long as half of elements exceed 5, it stays O(n^2).

# 2:
# No, the best case is 0(n) while the average and worse cases are 0(n^2)
# The if-condition is what causes the differences - the best case skips it entirely
# To make all three cases equivalent, remove the if-condition so the inner loop always runs

def processdata_equal(li):
    for i in range(len(li)):
        for j in range(len(li)):  # always runs, no condition
            li[i] *= 2

