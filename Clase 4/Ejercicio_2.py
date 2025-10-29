'''Write a script that will check whether
the entered number is even or odd and
display the appropriate message.'''

number = int(input("Enter a number to see if is it odd or even \n"))
if(number % 2 == 0):
    print('Number is even')
else:
    print('Number is odd')