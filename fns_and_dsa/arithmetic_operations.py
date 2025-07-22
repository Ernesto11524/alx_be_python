def perform_operation(num1, num2, operation):
    if operation in ['add', 'subtract', 'multiply', 'divide']:
        match(operation):
            case 'add': result = num1 + num2
            case 'subtract': result = num1 - num2
            case 'multiply': result = num1 * num2
            case 'divide': 
                    if (num2 != 0):
                        result = num1 / num2
                    else:
                         result = "Mass error"
    else:
         result = "Please enter the right operation(add, subtract, multiply, divide):"
    return result
                    