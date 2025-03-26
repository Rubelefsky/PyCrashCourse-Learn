# Page 17 - Modulo Operators
# % Modulo operators divides one number by another number and returns the remainder
number = input("Enter a number, and I'll tell you if it's even or odd.") # input assigned to number variable
number = int(number) # convert to integer

if number % 2 == 0: # Even numbers are always divisible by 2. If the modulo of a number and 2 is 0 the number is even.
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
