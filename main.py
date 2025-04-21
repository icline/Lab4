from FileGenerator import FileGenerator
from HeapSort import HeapSort
from ShellSort import ShellSort
from MergeSort import MergeSort
from InsertionSort import InsertionSort
from time import perf_counter

'''
Reads in one or more text files containing integers, and sorts the integers
in the file using Heap Sort, Shell Sort (with multiple sets of increments), 
Merge Sort, and Insertion Sort. Then compares the time each sorting 
algorithm took to complete the sort, and outputs the comparative results
to output.txt file. Also writes sorted numbers to output_<size>.txt files.

Input file names should be in the format "numbers_<size>_<order>.txt", where 
<size> is the number of integers, and <order> is either: "random", "ascending", 
or "reversed". 
'''
def main():
    
    # Expected file sizes and ordering types
    file_sizes = [25, 50, 200, 500, 2000]
    orders = ['random', 'reversed', 'ascending']
    
    # Create main output file for timings
    output_file = "output.txt"

    # Open output file as blank, ready for writing
    with open(output_file, 'w') as f:
        f.write("=" * 40 + "\n")
        f.write("Comparison of Heap, Shell, Merge and Insertion Sort\n")
        f.write("=" * 40 + "\n\n")
    
    # Iterate through all combinations of file sizes and orders
    for size in file_sizes:
        
        fg = FileGenerator(count=int(size))
        fg.generate()
        fg.reverse()
        fg.sort()

        # Create size-specific output file for sorted numbers
        sorted_output_file = f"output_{size}.txt"
        with open(sorted_output_file, 'w') as f:
            f.write(f"Sorted Numbers for Size {size}\n")
            f.write("=" * 40 + "\n\n")

        for order in orders:
            input_file = f"numbers_{size}_{order}.txt"
            
            # Read integers from input file, ignoring blank lines
            numbers = []
            try:
                with open(input_file, 'r') as f:
                    # Skip blank lines
                    for line in f:
                        if not line:
                            continue
                        line = line.strip()
                        numbers.append(int(line))
            except FileNotFoundError:
                with open(output_file, 'a') as f:
                    f.write(f"Input file {input_file} was not found.\n\n")
                continue
            except ValueError:
                with open(output_file, 'a') as f:
                    f.write(f"Invalid data in {input_file}\n\n")
                continue

            # Create instances of sorting classes
            heap_sorter = HeapSort(numbers.copy())
            shell_sorter_knuth = ShellSort()
            shell_sorter_set2 = ShellSort()
            shell_sorter_set3 = ShellSort()
            shell_sorter_set4 = ShellSort()
            merge_sorter = MergeSort()
            insertion_sorter = InsertionSort()

            # Run and time heap sort
            heap_start = perf_counter()
            heap_sorted = heap_sorter.heap_sort()  
            heap_end = perf_counter()
            heap_duration = heap_end - heap_start
            # Write heap sort results
            with open(sorted_output_file, 'a') as f:
                f.write(f"Heap Sort (File: {input_file})\n")
                f.write(f"{heap_sorted}\n\n")
            
            # Run and time Knuth sequence shell sort
            shell_start_knuth = perf_counter()
            shell_sorted_knuth = \
                shell_sorter_knuth.shell_sort(numbers.copy(), 'knuth') 
            shell_end_knuth = perf_counter()
            shell_duration_knuth = shell_end_knuth - shell_start_knuth
            # Write Knuth shell sort results
            with open(sorted_output_file, 'a') as f:
                f.write(f"Shell Sort Knuth (File: {input_file})\n")
                f.write(f"{shell_sorted_knuth}\n\n")
            
            # Run and time second increment set shell sort
            shell_start_2 = perf_counter()
            shell_sorted_2 = \
                shell_sorter_set2.shell_sort(numbers.copy(), 'set2') 
            shell_end_2 = perf_counter()
            shell_duration_2 = shell_end_2 - shell_start_2
            # Write set2 shell sort results
            with open(sorted_output_file, 'a') as f:
                f.write(f"Shell Sort Set2 (File: {input_file})\n")
                f.write(f"{shell_sorted_2}\n\n")

            # Run and time third increment set shell sort
            shell_start_3 = perf_counter()
            shell_sorted_3 = \
                shell_sorter_set3.shell_sort(numbers.copy(), 'set3') 
            shell_end_3 = perf_counter()
            shell_duration_3 = shell_end_3 - shell_start_3
            # Write set3 shell sort results
            with open(sorted_output_file, 'a') as f:
                f.write(f"Shell Sort Set3 (File: {input_file})\n")
                f.write(f"{shell_sorted_3}\n\n")

            # Run and time fourth increment set shell sort
            shell_start_4 = perf_counter()
            shell_sorted_4 = \
                shell_sorter_set4.shell_sort(numbers.copy(), 'hibbard') 
            shell_end_4 = perf_counter()
            shell_duration_4 = shell_end_4 - shell_start_4
            # Write hibbard shell sort results
            with open(sorted_output_file, 'a') as f:
                f.write(f"Shell Sort Hibbard (File: {input_file})\n")
                f.write(f"{shell_sorted_4}\n\n")

            # Run and calculate duration for Merge sort
            merge_start = perf_counter()
            merge_sorted = merge_sorter.merge_sort(numbers.copy())  
            merge_end = perf_counter()
            merge_duration = merge_end - merge_start
            # Write merge sort results
            with open(sorted_output_file, 'a') as f:
                f.write(f"Merge Sort (File: {input_file})\n")
                f.write(f"{merge_sorted}\n\n")

            # Run and calculate duration for Insertion sort
            insertion_start = perf_counter()
            insertion_sorted = \
                insertion_sorter.insertion_sort(numbers.copy())  
            insertion_end = perf_counter()
            insertion_duration = insertion_end - insertion_start
            # Write insertion sort results
            with open(sorted_output_file, 'a') as f:
                f.write(f"Insertion Sort (File: {input_file})\n")
                f.write(f"{insertion_sorted}\n\n")

            # Append timings to main output file
            with open(output_file, 'a') as f:
                f.write(f"File: {input_file}\n")
                f.write(f"File Size: {size}\n")
                f.write(f"Order: {order.capitalize()}\n")
                f.write(f"Heap Sort Duration: {(heap_duration * 1000):.4f} " 
                        f"milliseconds\n")
                f.write(f"Shell Sort Duration (Knuth): " 
                        f"{(shell_duration_knuth * 1000):.4f} milliseconds\n")
                f.write(f"Shell Sort Duration (Increment Set 2): " 
                        f"{(shell_duration_2 * 1000):.4f} milliseconds\n")
                f.write(f"Shell Sort Duration (Increment Set 3): " 
                        f"{(shell_duration_3 * 1000):.4f} milliseconds\n")
                f.write(f"Shell Sort Duration (Increment Set 4 AKA Hibbard): " 
                        f"{(shell_duration_4 * 1000):.4f} milliseconds\n")
                f.write(f"Merge Sort Duration: {(merge_duration * 1000):.4f} " 
                        f"milliseconds\n")
                f.write(f"Insertion Sort Duration: " 
                        f"{(insertion_duration * 1000):.4f} milliseconds\n\n")
                f.write("-" * 40 + "\n\n")

if __name__ == "__main__":
    main()