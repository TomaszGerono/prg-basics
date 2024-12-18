def f(number):
    # return True if the number is a Fibonacci number, or False otherwise
    def fib(n):


        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        else:
            return fib(n - 1) + fib(n)
        

    fib_list = []
    for i in range(1,number):
        fib_list.append(fib(i))

    if number in fib_list:
        return True
    
    else:
        return False
    
if __name__ == "__main__":
    print(f(5))
    print(f(4))