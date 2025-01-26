#
# def perform_operation(num1, num2, operation):
#     num1 = float(num1)
#     num2 = float(num2)
#     operation =str(operation)
#
#     match operation:
#         case "add":
#             print(f"Result: {num1 + num2}")
#
#         case "subtract":
#             print(f"Result: {num1 - num2}")
#
#         case "multiply":
#             print(f"Result: {num1 * num2}")
#
#         case "divide":
#             if num2 == 0:
#                 print("Cannot divide by zero.")
#             elif num2 !=0:
#                 result = num1 / num2
#                 print(f"The result is {result}")
#
#
# perform_operation(2, 4, "add")

def perform_operation(num1, num2, operation):

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"


