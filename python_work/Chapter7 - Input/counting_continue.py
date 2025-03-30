# Page 122

current_number = 0 # Set variable current_number to 0
while current_number < 10: # while loop if current number is less than 10
    current_number += 1 # increment count by 1
    if current_number % 2 == 0: # if modulo is 0 (divisible by 2), the continue statement tells Python to ifnore the rest of the loop and return to the beginning
        continue
    
    print(current_number)