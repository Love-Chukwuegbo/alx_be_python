def perform_operation(num1, num2, operation):
    if operation:   
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                result= "Unpermitted"
            else:
                result = num1 / num2
        return result
    else:
        print("please add an operation")
perform_operation(5.0,2.0, 'multiply')
