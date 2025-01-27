FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}F is {celsius}C")

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f"{celsius}C is {fahrenheit}F")

try:
    temperature = int(input("Enter the temperature to convert: "))
    cel_or_fahr = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if cel_or_fahr == "C":
        convert_to_fahrenheit(temperature)
    elif cel_or_fahr == "F":
        convert_to_celsius(temperature)
    else:
        print("input not accepted")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")





