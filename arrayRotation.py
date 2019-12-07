def arrayRotationByn(l, n):
    for x in range(n):
       y = l.pop(0)
       l.append(y)
        
    print(l)
        
l = [1,2,3,4,5,6,7]
arrayRotationByn(l,2)