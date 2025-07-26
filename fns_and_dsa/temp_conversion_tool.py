FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    # print(f"{farenheit}°F is {celsuis}°C")
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    # print(f"{celsius}°C is {fahrenheit}°F")
    return fahrenheit


while True:
    try:    
        temp = int(input("Enter the temperature to convert:"))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        assert unit == "C" or unit == "F" 
        break

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        continue

    except AssertionError:
        print("Invalid unit. Please enter 'C' or 'F'.")
        continue

if unit == "C":
    f = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {f}°F")
    
elif unit == "F":

    c =convert_to_celsius(temp)
    print(f"{temp}°F is {c}°C")
