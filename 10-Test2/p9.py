def f(arr):
    # Return the one number that is different from all the other numbers

    unique_numbers = set(arr)

    for num in arr:
        
        for unique_num in unique_numbers:

            count = 0

            if unique_num == num:
                count += 1

            if count < 1:
                return unique_num



if __name__ == "__main__":
    print(f([25,25,23]))
    print(f([7,7,7,7,7,5,7,7]))
    print(f([1,1,1,1,1,2]))
    