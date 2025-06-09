def perform_operation(num1,num2, operation=""):
    if operation:   
        match operation:
            case 'add':
                Result = num1 + num2
            case 'subtract':
                Result = num1 - num2
            case 'multiply':
                Result = num1 * num2
            case 'divide':
                if num2:
                    Result = num1 / num2
                else:
                    Result= "Division by zero is n"
        return Result
    else:
        print("please add an operation")
perform_operation(5.0,2.0, 'multiply')
