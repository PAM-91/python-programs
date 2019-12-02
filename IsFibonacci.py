def isfinonacci(x):
    a = 0
    b = 1
    
    while True:
        c = b
        b = a + b
        a = c
        if b > x:
            print("%d is not fibonacci number" % x)
            break
        elif b == x:
            print("%d is fibonacci number" % x)
            break
        
isfinonacci(22)
        