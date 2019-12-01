def isprime(x):
    flag = False
    for y in range(2,int(x/2),1):
        if x%y == 0:
            flag = True
    if flag == False:        
        print("%d is prime number" % x)
    else:
        print("{} is not prime number".format(x))
        
x = input("Enter a number to check its prime or not ")
y = int(x)
isprime(y)