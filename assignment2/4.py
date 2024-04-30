# Write a program that asks the user to enter two numbers and performs division. Handle any potential ZeroDivisionError and prompt the user to enter a valid divisor.
while True:    # start an infinite loop
    try:
        num1 = int(input("Enter the first number: "))  # ask the user to input the first number
        num2 = int(input("Enter the second number: "))  # ask the user to input the second number
        result = num1 / num2  # perform division
        break  # if the division is successful, break the loop
    except ValueError:  # if the user inputs a non-integer
        print("Invalid input. Please enter a valid integer.")  # print an error message
    except ZeroDivisionError:  # if the user tries to divide by zero
        print("Cannot divide by zero. Please enter a non-zero divisor.")  # print an error message

# after the loop ends, print the result
print(f"{num1} / {num2} = {result}")
