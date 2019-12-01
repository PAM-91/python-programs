def primenumber(start, end) :
    prime = []
    flag = 0
    y= 0
    for x in range(start,end):
        for y in range(2,int(x/2)):
            if x % y == 0:
                flag = 1
        
        if flag == 0 and x != 4 and x != 1:
            prime.append(x)
        flag = 0
    print(prime)

primenumber(1,10)