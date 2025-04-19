class SortError(Exception):
    """Base class for exceptions in sorting algorithms."""
    pass

class InvalidInputTypeError(SortError):
    """Raised when the input is not a list."""
    pass

class EmptyListError(SortError):
    """Raised when the input list is empty."""
    pass

class NonNumericElementError(SortError):
    """Raised when non-numeric elements are found in the list."""
    pass

class InconsistentTypeError(SortError):
    """Raised when elements in the list are not of the same type."""
    pass

class NoneValueError(SortError):
    """Raised when None is found in the list."""
    pass

class SortErrorHandler:
    """Input validation"""

    def validate_input(arr):
        # Check if input is a list
        if not isinstance(arr, list):
            raise InvalidInputTypeError("Input must be of type list.")

        # Check if list is empty
        if len(arr) == 0:
            raise EmptyListError("Input list is empty. Sorting not required.")

        # Check for None values
        if any(x is None for x in arr):
            raise NoneValueError("Input list contains None, which is not allowed.")

        # Check if all elements are numbers (int or float)
        for item in arr:
            if not isinstance(item, (int, float)):
                raise NonNumericElementError(f"Invalid item '{item}' found. All elements must be numeric.")

        # Check if all elements are the same data type
        first_type = type(arr[0])
        if not all(isinstance(x, first_type) for x in arr):
            raise InconsistentTypeError("All elements must be of the same type (all int or all float).")
        

