import re

def check_game(game, target_counts):
    for subset in game:
        cubes = re.findall(r'(\d+) (green|blue|red)', subset)
        for count, color in cubes:
            if int(count) > target_counts[color]:
                return False
    return True

def possible_games(input_data, target_counts):
    possible_game_ids = []

    for index, line in enumerate(input_data, start=1):
        game_id, subsets = line.split(":")
        game_id = int(game_id.split()[1])

        # Check if the game is possible
        if check_game(subsets.split(';'), target_counts):
            possible_game_ids.append(game_id)

    return possible_game_ids

# Read input data from the file
file_path = "strings.txt"
with open(file_path, "r") as file:
    input_data = [line.strip() for line in file]

# Target cube counts
target_counts = {'red': 12, 'green': 13, 'blue': 14}

# Get the list of possible game IDs
result = possible_games(input_data, target_counts)

# Print the result
print("The sum of the IDs of possible games is:", sum(result))
