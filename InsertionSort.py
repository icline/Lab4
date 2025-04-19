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