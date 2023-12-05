import re

file_path = "strings.txt"

with open(file_path, "r") as file:
    lines = file.read().splitlines()

winning_nums = []
card_nums = []
total = 0

for line in lines:
    parts = re.sub(r'Card[\s]+[\d]+: ', "", line).split(" | ")
    winning_nums.append(list(map(int, re.findall(r'[\d]+', parts[0]))))
    card_nums.append(list(map(int, re.findall(r'[\d]+', parts[1]))))

for i, card in enumerate(card_nums):
    matches = sum(1 for num in card if num in winning_nums[i])
    points = pow(2, matches - 1) if matches > 0 else 0
    total += points

print("The total points from the scratchcards are:", total)
