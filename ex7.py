import time
import random
import matplotlib.pyplot as plt


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node


    def get_size(self):
        count = 0
        curr = self.head

        while curr:
            count += 1
            curr = curr.next

        return count


    def get_element_at_pos(self, pos):
        curr = self.head
        for _ in range(pos):
            curr = curr.next
        return curr

    def reverse_slow(self):

        newhead = None
        prevNode = None
        size = self.get_size()

        for i in range(size - 1, -1, -1):

            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)

            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode

            prevNode = currNewNode

        self.head = newhead

    def reverse_fast(self):

        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev


def create_list(size):

    ll = LinkedList()

    for _ in range(size):
        ll.insert_tail(random.randint(1, 10000))

    return ll


def run_test():

    sizes = [1000, 2000, 3000, 4000]
    slow_times = []
    fast_times = []

    for size in sizes:

        slow_total = 0
        fast_total = 0

        for _ in range(100):

            ll1 = create_list(size)

            start = time.perf_counter()
            ll1.reverse_slow()
            end = time.perf_counter()
            slow_total += end - start


            ll2 = create_list(size)

            start = time.perf_counter()
            ll2.reverse_fast()
            end = time.perf_counter()
            fast_total += end - start


        slow_times.append(slow_total / 100)
        fast_times.append(fast_total / 100)


    plt.plot(sizes, slow_times, 'ro-', label="Slow reverse")
    plt.plot(sizes, fast_times, 'bo-', label="Fast reverse")

    plt.xlabel("List size")
    plt.ylabel("Time (seconds)")
    plt.title("Reverse Linked List Performance")
    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    run_test()