name = input("Enter your name: ")

if name == "":
    print("You did not enter your name")
    
else:
    print(f"Hello {name}")
    
################################################
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
else:
    print(f"Hello {name}")
    
###################################################
    
num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"You picked the number {num}")