import InsertionSort

class ShellSort:
    """
    Implements the Shell Sort algorithm with various increment sequences.
    Each method takes a list of integers as input and sorts the list in-place.
    """
    
    def __init__(self):
        # Define the different increment sequences
        self.knuth_increments = [1, 4, 13, 40, 121, 364, 1093, 3280, 9841, 29524]
        self.alt_increments1 = [1, 5, 17, 53, 149, 373, 1123, 3371, 10111, 30341]
        self.alt_increments2 = [1, 10, 30, 60, 120, 360, 1080, 3240, 9720, 29160]
        self.custom_increments = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]  # Powers of 2 minus 1
        
        # Create an instance of InsertionSort
        self.insertion_sorter = InsertionSort()
    
    def _get_applicable_increments(self, increments, array_size):
        """
        Gets increments that are smaller than the array size.
        Returns the increments in descending order.
        
        Args:
            increments: List of increment values
            array_size: Size of the array to be sorted
            
        Returns:
            List of applicable increments in descending order
        """
        applicable = [inc for inc in increments if inc < array_size]
        return sorted(applicable, reverse=True) if applicable else [1]  # Default to 1 if no applicable increments
    
    def shell_sort_knuth(self, arr):
        """
        Shell sort using Knuth's increment sequence: 1, 4, 13, 40, 121, 364, ...
        Sorts the array in-place.
        
        Args:
            arr: A list of integers to be sorted
            
        Returns:
            The same list, sorted in ascending order
        """
        increments = self._get_applicable_increments(self.knuth_increments, len(arr))
        
        for increment in increments:
            self.insertion_sorter.insertion_sort_with_increment(arr, increment)
        
        return arr
    
    def shell_sort_alt1(self, arr):
        """
        Shell sort using alternative sequence 1: 1, 5, 17, 53, 149, 373, ...
        Sorts the array in-place.
        
        Args:
            arr: A list of integers to be sorted
            
        Returns:
            The same list, sorted in ascending order
        """
        increments = self._get_applicable_increments(self.alt_increments1, len(arr))
        
        for increment in increments:
            self.insertion_sorter.insertion_sort_with_increment(arr, increment)
        
        return arr
    
    def shell_sort_alt2(self, arr):
        """
        Shell sort using alternative sequence 2: 1, 10, 30, 60, 120, 360, ...
        Sorts the array in-place.
        
        Args:
            arr: A list of integers to be sorted
            
        Returns:
            The same list, sorted in ascending order
        """
        increments = self._get_applicable_increments(self.alt_increments2, len(arr))
        
        for increment in increments:
            self.insertion_sorter.insertion_sort_with_increment(arr, increment)
        
        return arr
    
    def shell_sort_custom(self, arr):
        """
        Shell sort using a custom increment sequence: 1, 3, 7, 15, 31, 63, ...
        Sorts the array in-place.
        
        Args:
            arr: A list of integers to be sorted
            
        Returns:
            The same list, sorted in ascending order
        """
        increments = self._get_applicable_increments(self.custom_increments, len(arr))
        
        for increment in increments:
            self.insertion_sorter.insertion_sort_with_increment(arr, increment)
        
        return arr
    
    def shell_sort(self, arr, increment_type='knuth'):
        """
        General shell sort method that uses the specified increment sequence.
        
        Args:
            arr: A list of integers to be sorted
            increment_type: The type of increment sequence to use:
                           'knuth', 'alt1', 'alt2', or 'custom'
            
        Returns:
            The same list, sorted in ascending order
        """
        if increment_type == 'knuth':
            return self.shell_sort_knuth(arr)
        elif increment_type == 'alt1':
            return self.shell_sort_alt1(arr)
        elif increment_type == 'alt2':
            return self.shell_sort_alt2(arr)
        elif increment_type == 'custom':
            return self.shell_sort_custom(arr)
        else:
            # Default to Knuth's sequence
            return self.shell_sort_knuth(arr)