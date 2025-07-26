FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temp = 0

def convert_to_celsius(fahrenheit):
    global temp
    temp = fahrenheit
    celsius = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global temp
    temp = celsius
    fahrenheit = (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp = input("Enter the temperature to convert: ")
try:
    temp = int(temp)
    state = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if state == 'C':
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    elif state == 'F':
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    else:
        print("Please enter C or F")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")