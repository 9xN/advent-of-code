import re

def calculate_game_score(game):
    max_green, max_blue, max_red = 0, 0, 0

    for subset in game:
        cubes = re.findall(r'(\d+) (green|blue|red)', subset)
        for count, color in cubes:
            count = int(count)
            if color == 'green' and count > max_green:
                max_green = count
            elif color == 'blue' and count > max_blue:
                max_blue = count
            elif color == 'red' and count > max_red:
                max_red = count

    return max_green * max_blue * max_red

def total_score(input_data):
    index_sum = 0

    for index, line in enumerate(input_data, start=1):
        game_id, subsets = line.split(":")
        game_id = int(game_id.split()[1])

        # Calculate the score for the game
        game_score = calculate_game_score(subsets.split(';'))

        # Update the total sum
        index_sum += game_score

    return index_sum

# Read input data from the file
file_path = "strings.txt"
with open(file_path, "r") as file:
    input_data = [line.strip() for line in file]

# Get the total score using the provided logic
result = total_score(input_data)

# Print the result
print("The sum calculated using the provided logic is:", result)
