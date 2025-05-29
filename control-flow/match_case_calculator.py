num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
ops = input("Choose the operation (+, -, *, /):")
# print (num1 ops num2)
match ops:
    case "+" :
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/" if num2 != 0:
        result = num1 / num2
        print(f"The result is {result}")
    case "/" :
        print("Cannot divide by zero.")
    case _ :
        print("operation not included")