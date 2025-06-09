def perform_operation(num1, num2, operation):
    if operation:   
        match operation:
            case 'add':
                result = num1 + num2
            case 'subtract':
                result = num1 - num2
            case 'multiply':
                result = num1 * num2
            case 'divide':
                if num2:
                    result = num1 / num2
                else:
                    result= "Unpermitted"
        return result
    else:
        print("please add an operation")
perform_operation(5.0,2.0, 'multiply')
