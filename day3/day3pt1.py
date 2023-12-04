import re

def find_symbols(input_list, start_x, start_y, length):
    flag = False
    for i in range(-1, 2):
        row = ''
        for j in range(-1, length + 1):
            if (start_y + i >= 0 and start_y + i < len(input_list) and start_x + j >= 0 and start_x + j < len(input_list[start_y + i])):
                if (re.match(r'[^\d\.\n]', input_list[start_y + i][start_x + j])):
                    flag = True
    return flag

def sum_valid_numbers(input_list, num_positions):
    valid_nums = 0

    for index, pos_row in enumerate(num_positions):
        for num_info in pos_row:
            if find_symbols(input_list, num_info[0], index, num_info[1]):
                valid_nums += num_info[2]

    return valid_nums

# Read input data from the file
file_path = "strings.txt"
with open(file_path, "r") as file:
    lines = file.read().splitlines()

input_list = []
num_positions = []

for x in lines:
    input_list.append(x)
    temp_list = []
    for y in re.finditer(r"\d+", x):
        z = [y.start(), int(y.end() - y.start()), int(y.group())]
        temp_list.append(z)
    num_positions.append(temp_list)

# Get the sum of valid numbers
result = sum_valid_numbers(input_list, num_positions)

# Print the result
print("The sum of valid numbers in the engine schematic is:", result)
