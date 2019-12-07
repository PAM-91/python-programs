def maxElement(l):
    max = 0
    for x in l:
        if max < x :
            max = x
    print("Max Element is %d" % max)
    
l = [20, 10, 20, 4, 100]
maxElement(l)