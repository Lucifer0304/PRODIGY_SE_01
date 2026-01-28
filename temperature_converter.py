# Temperature Conversion Program

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


print("Temperature Conversion Program")
print("--------------------------------")
print("Select the original unit:")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

choice = int(input("Enter your choice (1/2/3): "))
temperature = float(input("Enter the temperature value: "))

print("\nConverted Temperatures:")

if choice == 1:
    print(f"Fahrenheit: {celsius_to_fahrenheit(temperature):.2f} °F")
    print(f"Kelvin: {celsius_to_kelvin(temperature):.2f} K")

elif choice == 2:
    print(f"Celsius: {fahrenheit_to_celsius(temperature):.2f} °C")
    print(f"Kelvin: {fahrenheit_to_kelvin(temperature):.2f} K")

elif choice == 3:
    print(f"Celsius: {kelvin_to_celsius(temperature):.2f} °C")
    print(f"Fahrenheit: {kelvin_to_fahrenheit(temperature):.2f} °F")

else:
    print("Invalid choice! Please select 1, 2, or 3.")
