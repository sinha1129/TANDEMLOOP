a = float(input('Enter a value: ')) # taking a as 1st input
b = float(input('Enter b value: ')) # taking b as 2nd input

operator = str(input('Ex: Addition/Subtraction/Multiplication/Division: ')) #taking operator as input lower or upper case


if operator.lower() == "addition": # converting the operator input into lowercase and printing the result as per the operator
    result = a + b
    print("addition: " + str(result))

elif operator.lower() == "subtraction":
    result = a - b
    print("subtraction: " + str(result))

elif operator.lower() == "multiplication":
    result = a * b
    print("multiplication: " + str(result))

elif operator.lower() == "division":
    result = a / b
    print("division: " + str(result))

else:
    print("Enter a valid operator")
