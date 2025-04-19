class MergeSort:
    """
    Implements the Merge Sort algorithm using an iterative approach.
    All methods process lists of integers and sort them in-place.
    """
    
    def __init__(self):
        pass
    
    def merge(self, arr, left, mid, right):
        """
        Merges two subarrays of arr[].
        First subarray is arr[left..mid]
        Second subarray is arr[mid+1..right]
        
        Args:
            arr: The array containing the subarrays to merge
            left: Starting index of the first subarray
            mid: Ending index of the first subarray
            right: Ending index of the second subarray
        """
        # Calculate sizes of the two subarrays to be merged
        n1 = mid - left + 1
        n2 = right - mid
        
        # Create temporary arrays
        L = [0] * n1
        R = [0] * n2
        
        # Copy data to temporary arrays L[] and R[]
        for i in range(n1):
            L[i] = arr[left + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]
        
        # Merge the temporary arrays back into arr[left..right]
        i = 0       # Initial index of first subarray
        j = 0       # Initial index of second subarray
        k = left    # Initial index of merged subarray
        
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Copy the remaining elements of L[], if any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        
        # Copy the remaining elements of R[], if any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    
    def merge_sort(self, arr):
        """
        Main function to sort an array using merge sort with an iterative approach.
        
        Args:
            arr: A list of integers to be sorted
            
        Returns:
            The same list, sorted in ascending order
        """
        n = len(arr)
        # Start with size of subarrays as 1 and merge them
        curr_size = 1
        
        # Merge subarrays in bottom-up manner
        # First merge subarrays of size 1 to create sorted subarrays of size 2,
        # then merge subarrays of size 2 to create sorted subarrays of size 4, and so on
        while curr_size < n:
            # Pick starting point of different subarrays of current size
            left = 0
            while left < n - 1:
                # Find ending point of left subarray
                mid = min(left + curr_size - 1, n - 1)
                
                # Find ending point of right subarray
                right = min(left + 2 * curr_size - 1, n - 1)
                
                # Merge subarrays arr[left...mid] & arr[mid+1...right]
                self.merge(arr, left, mid, right)
                
                # Move to next pair of subarrays
                left += 2 * curr_size
            
            # Increase size of subarrays to be merged
            curr_size = 2 * curr_size
        
        return arr