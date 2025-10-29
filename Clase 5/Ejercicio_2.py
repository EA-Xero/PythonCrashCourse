"""Print all odd numbers less than 100.
(write two versions of the code:
one using the continue operator,
and
the other without this operator)."""

print("\nThis count is made by using a while loop with continue \n")
i = 0
while(i < 101):
    i+=1
    if(i % 2 != 0):
        print(f"Value of i:{i}")
    else:
        continue

print("\nThis count is made by using a while loop without continue \n")
i = 0
while(i < 101):
    i+=1
    if(i % 2 != 0):
        print(f"Value of i:{i}")
    else:
        continue