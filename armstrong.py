def armstrong(n):
    x = str(n)
    z = 0
    power = 0
    for i in x:
        power += 1
        
    for i in x:
        z += pow(int(i),power)
    
    if z == n :
        print("armstrong")
    else :
        print("No armstrong")   

armstrong(153)