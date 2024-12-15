
number = int(input("Enter the number: "))
limit = int(input("Enter the limit: "))


print(f"Multiplication table of {number} up to {limit}:")
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")
