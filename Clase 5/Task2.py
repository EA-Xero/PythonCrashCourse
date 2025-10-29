'''Print Fibonacci numbers up to the entered number n'''
def fibonacci(n):
    a, b = 0, 1  # First two Fibonacci numbers
    while a <= n:
        print(f"Fibonacci: {a}")
        a, b = b, a + b  # Update to next Fibonacci numbers

n = int(input("Enter the maximum value of Fibonacci number to seek: "))
fibonacci(n)


