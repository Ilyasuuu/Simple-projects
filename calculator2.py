def add(*numbers):
    return sum(numbers)

def substraction(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def division(number1, number2):
    if number2 == 0:
        return "Error: Division by zero"
    else:
        return number1 / number2


print("Welcome to my simple calculator, simple human")
print("Let's do some math")

while True:
    print("A+: + Addition")
    print("S-: - Substraction")
    print("M*: * Multiplication")
    print("D/: / Division")
    operation = input("Choose what do you want to start with A+/S-/M*/D/: ")

    try: 
        if operation.upper() == "A+":
            user_input = input("Enter numbers separated by '+': ")
            numbers_str = user_input.split("+")
            number = [float(num) for num in numbers_str]
            result = add(*number)
            print("The result is:", result)

        elif operation.upper() == "S-":
            user_input = input("Enter numbers separated by '-': ")
            numbers_str = user_input.split("-")
            number = [float(num) for num in numbers_str]
            result = substraction(*number)
            print("The result is: ", result)

        elif operation.upper() == "M*":
            user_input = input("Enter numbers separated by '*': ")
            numbers_str = user_input.split("*")
            number = [float(num) for num in numbers_str]
            result = multiply(*number)
            print("The result is: ", result)

        elif operation.upper() == "D/":
            user_input = input("Enter 2 numbers separated by '/': ")
            numbers_str = user_input.split("/")
            if len(numbers_str) == 2:
                number1, number2 = float(numbers_str[0]), float(numbers_str[1])
                result = division(number1, number2)
                print("The result is:", result)
            else:
                print("Please enter exactly two numbers.")    

        else:
            print("Invalid operation selected. Please choose A+, S-, M*, or D/.")

    except ValueError:
        print("Valid Numbers")

    another_calculation = input("Do you want to do another operation? (yes/no): ")
    if another_calculation.lower() != "yes":
        break


print("try harder next time, see you next time")




        
    