'''Write a script, which of the two entered
numbers will determine which of them is
more and which is less. Take into account
the case of equality of numbers'''

number1 = int(input("Enter number1 \n"))
number2 = int(input("Enter number2 \n"))

if(number1 == number2):
    print("The numbers are equal")
elif(number1 > number2):
    print("Number1 is greater than Number2")
else:
    print("Number2 is greater than Number1")