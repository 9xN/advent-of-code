import re

def find_symbols(input_list, start_x, start_y, length, value, gears_found):
    for i in range(-1, 2):
        row = ''
        for j in range(-1, length + 1):
            if (start_y + i >= 0 and start_y + i < len(input_list) and start_x + j >= 0 and start_x + j < len(input_list[start_y + i])):
                if (re.match(r'[\*]', input_list[start_y + i][start_x + j])):
                    key = fr'{start_y + i},{start_x + j}'
                    if key in gears_found:
                        gears_found[key].append(value)
                    else:
                        gears_found[key] = [value]

def calculate_total_gears(input_list, num_positions):
    gears_found = {}

    for index, pos_row in enumerate(num_positions):
        for num_info in pos_row:
            find_symbols(input_list, num_info[0], index, num_info[1], num_info[2], gears_found)

    total = 0

    for k in gears_found:
        if len(gears_found[k]) == 2:
            total += gears_found[k][0] * gears_found[k][1]

    return total

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

# Calculate the total gears
result = calculate_total_gears(input_list, num_positions)

# Print the result
print("The total calculated using the provided logic is:", result)
