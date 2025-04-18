a = int(input("Enter a number: "))  # Take input from the user

output = []  # Create an empty list to store the output numbers


for i in range(a): # Loop to generate 'a' numbers
    odd = 2 * i + 1  # Generate the i+1 number
    output.append(str(odd))  # Convert to string and add to list


print(", ".join(output)) # Join the list with commas and print the result