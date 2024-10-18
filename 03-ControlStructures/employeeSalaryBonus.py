basicSalary = 5000
totalSalary = 0
isBonus = True
bonus = 0.15 # (15%)

if isBonus:
    totalSalary = basicSalary + basicSalary*bonus

else:
    totalSalary = basicSalary
    
print(f'Basic salary: {basicSalary}')
print(f'Bonus included? {isBonus}')
print(f'Total salary: {totalSalary}')