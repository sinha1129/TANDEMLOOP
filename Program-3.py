# Take input from the user
a = int(input("Enter a number: "))


if a % 2 == 0:
    a = a - 1  # Adjust 'a' if it's even and Use the previous odd number

# Create an empty list to store the odd numbers
output = []

# Generate the odd number sequence
for i in range(a):
    odd = 2 * i + 1
    output.append(str(odd))


print(", ".join(output))  # Display the output
