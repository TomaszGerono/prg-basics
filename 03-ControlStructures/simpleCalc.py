number1 = int(input('Enter x: '))
number2 = int(input('Enter y: '))
operator = input('Enter operator (+,-,*,/): ')

match operator:
    case '+':
        print(f'{number1} {operator} {number2} = {number1+number2}')
    
    case '-':
        print(f'{number1} {operator} {number2} = {number1-number2}')
        
    case '*':
        print(f'{number1} {operator} {number2} = {number1*number2}')
        
    case '/':
        print(f'{number1} {operator} {number2} = {number1/number2}')