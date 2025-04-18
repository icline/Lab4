import sys

from typing import List

class HeapSort:

    class Node:

        def __init__(self, data=0):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self, array):
        self.array = array
        self.root = None

    def heapify(self):
        # Creates a Min Heap
        last_non_leaf = (len(self.array)//2) - 1
        for i in range(last_non_leaf, -1, -1):
            heapifying = True
            index = i
            while heapifying is True:
                biggest = index
                left_child = 2*index + 1
                right_child = (2*index) + 2

                bigger_nodes = 0
                if len(self.array) > left_child and self.array[left_child] < self.array[index]:
                    biggest = left_child
                    bigger_nodes += 1

                if len(self.array) > right_child and self.array[right_child] < self.array[biggest]:
                    biggest = right_child
                    bigger_nodes += 1
                
                if bigger_nodes > 0:
                    self.array[index], self.array[biggest] = self.array[biggest], self.array[index]
                    index = biggest
                    bigger_nodes = 0
                else:
                    heapifying = False


    def heap_sort(self):
        print('Original Array:')
        print(self.array)

        # Create Heap
        self.heapify()
        print('Min Heap (represented as an array):')
        print(self.array)

        # Sort
        sorted_array = []
        while self.array:
            self.array[0], self.array[-1] = self.array[-1], self.array[0]
            sorted_array.append(self.array.pop())
            self.heapify()

        print('Sorted Array:')
        print(*sorted_array)
        return sorted_array


if __name__ == "__main__":
    input_file = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')
    
    values = []
    for line in input_file:
        number = line.strip()
        values.append(int(number))

    heap = HeapSort(values)
    results = heap.heap_sort()
    results = str(results)
    output_file.write(results)

    input_file.close()
    output_file.close()
        
            

