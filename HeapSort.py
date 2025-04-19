class HeapSort:
    """
    Implements the Heap Sort algorithm.
    All methods process lists of integers and sort them in-place.
    """
    
    def __init__(self):
        pass
    
    def heapify(self, arr, n, i):
        """
        Heapify subtree rooted at index i.
        n is the size of the heap.
        
        Args:
            arr: The array representing the heap
            n: The size of the heap (usually len(arr))
            i: The index of the root of the subtree to heapify
        """
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # Left child = 2*i + 1
        right = 2 * i + 2  # Right child = 2*i + 2
        
        # See if left child of root exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        # See if right child of root exists and is greater than root
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        # Change root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            # Heapify the affected sub-tree
            self.heapify(arr, n, largest)
    
    def build_heap(self, arr):
        """
        Builds a max heap from an unordered array.
        
        Args:
            arr: A list of integers to be turned into a heap
        """
        n = len(arr)
        # Build heap (rearrange array)
        # Start from the last non-leaf node and work up to the root
        # Last non-leaf node is at index (n//2)-1
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
    
    def heap_sort(self, arr):
        """
        Main function to sort an array using heap sort.
        Sorts the array in-place.
        
        Args:
            arr: A list of integers to be sorted
            
        Returns:
            The same list, sorted in ascending order
        """
        n = len(arr)
        
        # Build a maxheap
        self.build_heap(arr)
        
        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
            self.heapify(arr, i, 0)  # Call heapify on the reduced heap
        
        return arr