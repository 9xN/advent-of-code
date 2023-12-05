import re

file_path = "strings.txt"

with open(file_path, "r") as file:
    lines = file.read().splitlines()

winning_nums = []
card_nums = []

def get_matches(w_nums, c_nums):
    matches = 0
    for num in c_nums:
        if num in w_nums:
            matches += 1
    return matches

for line in lines:
    parts = re.sub(r'Card[\s]+[\d]+: ', "", line).split(" | ")
    winning_nums.append(list(map(int, re.findall(r'[\d]+', parts[0]))))
    card_nums.append(list(map(int, re.findall(r'[\d]+', parts[1]))))

match_nums = []
copy_nums = [1] * len(winning_nums)

for i, card in enumerate(card_nums):
    match_nums.append(get_matches(winning_nums[i], card))

for i, matches in enumerate(match_nums):
    for k in range(0, copy_nums[i]):
        for j in range(i, matches + i):
            copy_nums[j + 1] += 1

total_points = sum(copy_nums)

print("The total points from the scratchcards are:", total_points)
