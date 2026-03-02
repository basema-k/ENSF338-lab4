import time
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert(self, data):
        # Insert at end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def get(self, index):
        # Get node at index
        if index < 0 or index >= self.size:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
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
    

# to be completed
'''
def measure_time(data_struct, search_func, data, target):
    # Fill the structure
    for val in data:
        data_struct.insert(val)
    
    # Time the search
    start = time.time()
    search_func(target)
    end = time.time()
    
    return (end - start) * 1_000_000  # microseconds

def run_test():
    sizes = [1000, 2000, 4000, 8000]
    ll_times = []
    array_times = []
    
    print("\n" + "="*50)
    print("PERFORMANCE RESULTS")
    print("="*50)
    
    for size in sizes:
        # Create sorted data
        data = sorted([random.randint(1, 10000) for _ in range(size)])
        target = random.choice(data)  # Pick existing number
        
        # Test Linked List
        ll = LinkedList()
        ll_time = measure_time(ll, ll.binary_search, data, target)
        ll_times.append(ll_time)
        
        # Test Array
        arr = Array()
        arr_time = measure_time(arr, arr.binary_search, data, target)
        array_times.append(arr_time)
        
        print(f"Size {size}:")
        print(f"  Linked List: {ll_time:.2f} μs")
        print(f"  Array:       {arr_time:.2f} μs")
        print(f"  Ratio:       {ll_time/arr_time:.1f}x slower")
    
    # Plot results
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, ll_times, 'bo-', label='Linked List', linewidth=2)
    plt.plot(sizes, array_times, 'ro-', label='Array', linewidth=2)
    plt.xlabel('Input Size')
    plt.ylabel('Time (microseconds)')
    plt.title('Binary Search Performance')
    plt.legend()
    plt.grid(True)
    plt.savefig('performance.png')
    plt.show()

if __name__ == "__main__":
    print("="*50)
    print("EXERCISE 1: Binary Search")
    print("="*50)
    
    # Simple demo
    print("\nDemo with small list:")
    ll = LinkedList()
    for x in [1, 3, 5, 7, 9, 11, 13, 15]:
        ll.insert(x)
    
    print(f"Search for 7: {'Found' if ll.binary_search(7) else 'Not found'}")
    print(f"Search for 8: {'Found' if ll.binary_search(8) else 'Not found'}")
    
    # Run performance test
    run_test()

    '''