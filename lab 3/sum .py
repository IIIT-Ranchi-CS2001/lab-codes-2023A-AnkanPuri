
number = int(input("Enter a number: "))

original_number = number
digit_sum = 0

while number > 0:
    digit = number % 10   
    digit_sum += digit  
    number = number // 10  


print(f"The number is: {original_number}")
print(f"The sum of the digits is: {digit_sum}")

