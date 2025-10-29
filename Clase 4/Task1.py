"Temperature Converter"

"""Write a Python program that prompts the user to enter a temperature in Celsius and then
converts it to Fahrenheit using the formula: F = (C * 9/5) + 32. Your program should then
print out the converted temperature in Fahrenheit.
However, if the user enters a temperature below -273.15°C (the lowest possible
temperature in the universe, also known as absolute zero), your program should print an
error message instead of attempting to convert the temperature."""

temperatureC = float(input("Enter a Temparute in Celsius, without format identifier (C°):\n"))
if(temperatureC <= -273.15):
    print("inserted temperature is not valid \n")
    print("Keep in mind, the absolute cero in the universe is -273.15 celsius \n")
else:
    temperatureF = (temperatureC * 9/5 ) + 32
    print(f"The temperature inserted in Fahrenheit is: {temperatureF} \n")
