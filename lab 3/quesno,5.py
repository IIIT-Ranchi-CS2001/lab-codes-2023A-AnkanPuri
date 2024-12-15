
input_string = input("Enter a string: ")

for char in input_string:
    if not char.isalnum():  
        print(False)
        break
else:

    print(True)
