driving_mode = input('Enter driving mode (A/M/E):')
distance = int(input('Enter distance in km: '))
fuel_consumption = 0 # per 100 km

match driving_mode:
    case 'A':
        fuel_consumption = 7
    
    case 'M':
        fuel_consumption = 9
        
    case 'E':
        fuel_consumption = 6
        
# fuel_consumption_per_1_km = fuel_consumption / 100
total_consumption = distance * (fuel_consumption / 100)

print(f'Total fuel consumption over a distance of {distance} km')
print(f'in driving mode {driving_mode} is {int(total_consumption)}')