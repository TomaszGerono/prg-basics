def f(x,y):
    # Returns a number denoting the quadrant of the coordinate system in which the point is located

    if x > 0 and y > 0:
        return 1
    
    if x > 0 and y < 0:
        return 4
    
    if x < 0 and y < 0:
        return 3
    
    if x < 0 and y > 0:
        return 2
    

if __name__ == "__main__":
    print(f(5,2))
    print(f(-5,2))
    print(f(5,-2))