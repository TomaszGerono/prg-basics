size = input('Enter size symbol: ')

match size:
    case 'S':
        print('S: Small size')

    case 'M':
        print('M: Medium size')
        
    case "L":
        print('L: Large size')
    
    case "XL":
        print('XL: Extra large size')
        
    case _:
        print('Incorrect symbol')