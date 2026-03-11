
1. Advantages and disadvantages of arrays vs linked lists

Arrays:

    Advantages
    - Fast access using indexing (O(1))
    - Elements stored next to each other in memory
    - Binary search is efficient on sorted arrays

    Disadvantages
    - Need to shift elements to insert or delete in the middle (O(n))
    - May require resizing when capacity is exceeded

Linked Lists

    Advantages
    - Inserting and deleting is efficient (O(1)) if desired position is known
    - Dont need to shift elements
    - Dynamically allocated, dont need to resize

    Disadvantages
    - To access elements one must traverse from head pointer (O(n))
    - More memory intensive since each node stores both a value and a pointer
    - Binary search is inefficient because random access is not possible

2. Efficient implementation of replace() for arrays

In an array we just need to overwrite the existing element: arr[i] = new_value
With an array there is no need to shift elements and therefore there is a lower complexity.

3. Feasibility of sorting algorithms on a doubly linked list

Insertion sort: This algorithm is feasible for a doubly linked list because nodes can be inserted in the correct position by updating the previous and next pointers. No shifting of elements is required.

Merge sort: This algorithm is also feasible for a doubly linked list because the list can be divided into smaller lists and then merged by adjusting pointers between nodes instead of moving elements.

4. Complexity comparison

Algorithm	        Linked List	    Array
Insertion Sort	    O(n²)	        O(n²)
Merge Sort	        O(n log n)	    O(n log n)

(Merge sort is still usually more efficient on linked lists because it doesnt require shifting elements or extra copying)