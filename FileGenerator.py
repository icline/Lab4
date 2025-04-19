import random

class FileGenerator:
    def __init__(self, file_number=1, count=100, min_val=1, max_val=1000):
        self.file_number = file_number
        self.count = count
        self.min_val = min_val
        self.max_val = max_val
        self.input_file = f"numbers_{file_number}.txt"
        self.reversed_file = f"numbers_{file_number}_reversed.txt"
        self.sorted_file = f"numbers_{file_number}_sorted.txt"

    # Method to generate random numbers
    def generate(self):
        numbers = [random.randint(self.min_val, self.max_val) for _ in range(self.count)]

        with open(self.input_file, 'w') as f:
            for num in numbers:
                f.write(f"{num}\n")

    # Method to reverse numbers from input file
    def reverse(self):
        try:
            with open(self.input_file, 'r') as f:
                numbers = [line.strip() for line in f if line.strip()]

            reversed_numbers = list(reversed(numbers))

            with open(self.reversed_file, 'w') as f:
                for num in reversed_numbers:
                    f.write(f"{num}\n")

        except FileNotFoundError:
            print(f"File {self.input_file} not found.")

    # Method to sort numbers from input file
    def sort(self):
        try:
            with open(self.input_file, 'r') as f:
                numbers = [int(line.strip()) for line in f if line.strip()]

            sorted_numbers = sorted(numbers)

            with open(self.sorted_file, 'w') as f:
                for num in sorted_numbers:
                    f.write(f"{num}\n")

        except FileNotFoundError:
            print(f"File {self.input_file} not found.")


fg = FileGenerator(file_number=2, count=10)
fg.generate()
fg.reverse()
fg.sort()
