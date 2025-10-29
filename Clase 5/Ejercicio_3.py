"""Check if the list contains odd numbers.
(Hint: use the break statement)"""

numbers = []

while True:
    num = input("Enter a number (or type 'end' to finish): ")
    if num.lower() == 'end':
        break
    numbers.append(int(num))

print("\nFinal list:\n", numbers)

count = 0
for number in numbers:
    if( number % 2 != 0):
        print(f"Number {number} is and odd number")
        count+=1

print(f"\nThere is {count} odds numbers in the list\n")