class InsertionSort:
    """
    Implements the Insertion Sort algorithm.
    All methods process lists of integers and sort them in-place.
    """
    
    def __init__(self):
        pass
    
    def insertion_sort(self, arr):
        """
        Main function to sort an array using insertion sort.
        Sorts the array in-place.
        
        Args:
            arr: A list of integers to be sorted
            
        Returns:
            The same list, sorted in ascending order
        """
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            key = arr[i]  # Element to be inserted in the sorted sequence
            
            # Move elements of arr[0..i-1] that are greater than key
            # to one position ahead of their current position
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        
        return arr
    
    def insertion_sort_with_increment(self, arr, increment):
        """
        Modified insertion sort that operates on subarrays with a specific gap/increment.
        Used by Shell Sort to sort elements that are 'increment' positions apart.
        This creates h-sorted arrays, where h is the increment value.
        
        For each position starting at 'increment', this method:
        1. Takes the element at that position as the key
        2. Compares it with elements that are 'increment' positions before it
        3. Shifts larger elements forward by 'increment' positions
        4. Places the key in its correct position within its subarray
        
        Args:
            arr: A list of integers to be sorted
            increment: The gap between elements to be compared
            
        Returns:
            The same list, with all elements spaced 'increment' apart properly sorted
        """
        for i in range(increment, len(arr)):
            key = arr[i]
            j = i
            # Compare and shift elements that are 'increment' positions apart
            while j >= increment and arr[j - increment] > key:
                arr[j] = arr[j - increment]
                j -= increment
            arr[j] = key
        return arr
