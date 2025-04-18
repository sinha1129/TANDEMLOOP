# Define the list of numbers
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Create an empty dictionary to store the counts
# The keys will be numbers from 1 to 9
# The values will be how many times numbers in the list are divisible by that key
divisible_counts = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}

# Go through each number in the list
for number in numbers:
    
    # Check if this number is divisible by 1 through 9
    for divisor in range(1, 10):  # 1 to 9 inclusive
        if number % divisor == 0:
            # If divisible, increase the count for that divisor
            divisible_counts[divisor] += 1

# Print the final dictionary
print("Output:")
print(divisible_counts)
