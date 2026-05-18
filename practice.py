# Python compound interest calculator
#A = P(1 + r/n)^t

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter principle amount: "))
    if principle < 0:
        print("Principle amount cannot be less than 0")
    else:
        break

while True:
    rate = float(input("Enter interest rate amount: "))
    if rate < 0:
        print("interest rate cannot be less than 0")
    else:
        break  
    
while True:
    time = float(input("Enter time in years: "))
    if time < 0:
        print("time cannot be less than 0")
    else:
        break
    
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: R{total:.2f}")