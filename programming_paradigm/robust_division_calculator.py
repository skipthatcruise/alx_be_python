def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
        return

    try:
       print(f"The result of the division is {(numerator / denominator)}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return