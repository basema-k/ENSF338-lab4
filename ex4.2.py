import timeit
import matplotlib.pyplot as plt
import random

# 3. Searching in a sorted array:
# inefficient: Linear search - scan every element one by one
# efficient: Binary search - repeatedly half the search space

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 4. Worst-case complexity:
# Linear search: O(n) - target is the last element or not present at all, must scan every element
# Binary search: O(log n) - each step halfs the remaining search space. Max you can keep halving until findind the target is log2(n)

# 5 :

N = 10000          # array size
MEASUREMENTS = 200  # number of timed runs each

arr = list(range(N))           
target = -1                    # worst case: target not in array

timer_linear = timeit.Timer(
    stmt="linear_search(arr, target)",
    globals={"linear_search": linear_search, "arr": arr, "target": target}
)

timer_binary = timeit.Timer(
    stmt="binary_search(arr, target)",
    globals={"binary_search": binary_search, "arr": arr, "target": target}
)

times_linear = [t * 1e6 for t in timer_linear.repeat(repeat=MEASUREMENTS, number=1)]
times_binary = [t * 1e6 for t in timer_binary.repeat(repeat=MEASUREMENTS, number=1)]

print(f"Linear search — average: {sum(times_linear)/len(times_linear):.2f} µs")
print(f"Binary search — average: {sum(times_binary)/len(times_binary):.2f} µs")

plt.figure(figsize=(9, 4))

plt.subplot(1, 2, 1)
plt.hist(times_linear, bins=30, color="tomato", alpha=0.8)
plt.xlabel("Time (µs)")
plt.ylabel("Frequency")
plt.title(f"Linear Search O(n)\nn={N}, {MEASUREMENTS} measurements")

plt.subplot(1, 2, 2)
plt.hist(times_binary, bins=30, color="steelblue", alpha=0.8)
plt.xlabel("Time (µs)")
plt.ylabel("Frequency")
plt.title(f"Binary Search O(log n)\nn={N}, {MEASUREMENTS} measurements")

plt.tight_layout()
plt.savefig("ex4.2_plot.png", dpi=150)
plt.show()