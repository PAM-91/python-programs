def nthfibonacciNum(n):
    a = 0
    b = 1
    
    if n < 0 :
        print("Invalid Input")
    elif n == 0:
        print("%d nth fibonacciNum " % 0)
    elif n == 1:
        print("%d nth fibonacciNum " % 1)
    else :
        for x in range(2, n):
            c = b
            b = a + b
            a = c
    
    print("%d nth fibonacciNum " % b)
    
nthfibonacciNum(9)