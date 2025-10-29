'''Print all even numbers less than 100
(write two variants of the code:
one using the while loop,
and
the other using the for loop)'''

print("\nThis count is made by using a while loop \n")
i = 0
while(i < 101):
    if(i % 2 == 0):
        print(f"Value of i:{i}")
    i+=1


print("\nThis count is made by using a for loop\n")
z = 0
for z in range (101):
    if(z % 2 == 0):
        print(f"Value of z:{z}")
    z+=1
