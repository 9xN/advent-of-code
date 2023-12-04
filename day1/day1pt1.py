def sum_calibration_values(calibration_document):
    total_sum = 0

    for line in calibration_document:
        # Find the first and last digits
        first_digit = next((c for c in line if c.isdigit()), None)
        last_digit = next((c for c in reversed(line) if c.isdigit()), None)

        # If both first and last digits are found, convert to a two-digit number and add to the total sum
        if first_digit is not None and last_digit is not None:
            calibration_value = int(first_digit + last_digit)
            total_sum += calibration_value

    return total_sum

# Read calibration document from the file
file_path = "strings.txt"
with open(file_path, "r") as file:
    calibration_document = [line.strip() for line in file]

# Calculate the sum of calibration values
result = sum_calibration_values(calibration_document)

# Print the result
print("The sum of all calibration values is:", result)
