def f(array2D):
    # Return how many people remained on the bus

    # [ [2,0],[3,1] ] means that at the first stop
    # 2 people got on and 0 got off, and at the second
    # stop 3 people got on and 1 got off

    total_people = 0

    for row in array2D:
        total_people += row[0]
        total_people -= row[1]

    return total_people



if __name__ == "__main__":
    print(f([[3,0]]))
    print(f([ [3,0] , 
              [6,1] ]))