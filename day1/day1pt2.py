import re

def convert_to_numbers(input_str):
    # Replace spelled-out digits with corresponding numeric representations
    conversion_dict = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
    for word, replacement in conversion_dict.items():
        input_str = re.sub(word, replacement, input_str)

    # Remove non-numeric characters
    numeric_str = re.sub(r'[^0-9]', '', input_str)

    # Extract the first and last digits and form a two-digit number
    if numeric_str:
        return int(numeric_str[0] + numeric_str[-1])
    else:
        return 0

# Read input from the file
file_path = "strings.txt"
with open(file_path, "r") as file:
    lines = file.readlines()

# Convert lines to a list of numbers using the provided logic
numbers = [convert_to_numbers(line) for line in lines]

# Calculate the sum of the numbers
total_sum = sum(numbers)

# Print the result
print("The sum of all calibration values is:", total_sum)
