import time
import random
import matplotlib.pyplot as plt
import numpy as np


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        self.size += 1

    def get(self, index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def binary_search(self, target):
        left = 0
        right = self.size - 1

        while left <= right:
            mid = (left + right) // 2
            mid_node = self.get(mid)

            if mid_node.data == target:
                return True
            elif mid_node.data < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


class Array:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def binary_search(self, target):
        left = 0
        right = len(self.data) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.data[mid] == target:
                return True
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
    

def run_test():

    sizes = [1000, 2000, 4000, 8000]
    ll_times = []
    arr_times = []

    for size in sizes:

        data = sorted(random.randint(1, 10000) for _ in range(size))

        ll = LinkedList()
        arr = Array()

        for v in data:
            ll.insert(v)
            arr.insert(v)

        ll_total = 0
        arr_total = 0
        tests = 100

        for _ in range(tests):

            target = random.randint(1, 10000)

            start = time.perf_counter()
            ll.binary_search(target)
            end = time.perf_counter()
            ll_total += (end - start) * 1_000_000

            start = time.perf_counter()
            arr.binary_search(target)
            end = time.perf_counter()
            arr_total += (end - start) * 1_000_000

        ll_times.append(ll_total / tests)
        arr_times.append(arr_total / tests)

    # Plot results
    plt.plot(sizes, ll_times, 'bo-', label="Linked List")
    plt.plot(sizes, arr_times, 'ro-', label="Array")

    # Interpolation
    x = np.linspace(min(sizes), max(sizes), 100)

    ll_fit = np.poly1d(np.polyfit(sizes, ll_times, 2))
    arr_fit = np.poly1d(np.polyfit(sizes, arr_times, 1))

    plt.plot(x, ll_fit(x), 'b--')
    plt.plot(x, arr_fit(x), 'r--')

    plt.xlabel("Input Size")
    plt.ylabel("Time (microseconds)")
    plt.title("Binary Search Performance")
    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    run_test()

"""
The complexity of binary search on a linked list is O(n).

Binary search requires accessing the middle element repeatedly.
In an array this is O(1), but in a linked list we must traverse
the list from the head to reach the middle node, which costs O(n).
The total cost becomes n + n/2 + n/4 + ... ≈ 2n

As a result, the overall complexity is O(n).
"""