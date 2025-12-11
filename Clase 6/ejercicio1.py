'''Task1. 
In the range from 1 to 10 determine
• even numbers that are divisible by 2,
• odd numbers, which are divisible by 3,
• numbers that are not divisible by 2 and 3.'''

even = []
odd = []
Nnot = []
for x in range(10):
    if(x == 0):
        continue
    if(x % 2 == 0):
        even.append(x)
    elif(x % 3 == 0):
        odd.append(x)
    else:
        Nnot.append(x)

print(f'Even numbers:{even}')
print(f'Odd divisible numbers:{odd}')
print(f'Not divisible numbers (or prime numbers):{Nnot}')