'''Create a list that contains elements of integer type, then
use the loop to change the type of these elements to a floating
type.'''
numbers = []
while True:
    number = input("Insert number or type 'end' to finalize the insertion: ")
    if(number.lower() == 'end'):
        break
    elif (int(number)):
        numbers.append(int(number))
        continue

print(f"\ncomplete list with int numbers: {numbers}\n")

numbers = [float(n) for n in numbers]
print(f"\ncomplete list with float numbers: {numbers}\n")