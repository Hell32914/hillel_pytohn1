x = [0,1,7,2,4,8]
# x = [1,3,5]
# x = [6]
# x = []

if (len(x)) == 0:
    print(x)

elif (len(x)) == 1: 
    res = x[0] * x[0] 
    print(res)
    
elif (len(x)) >= 2: 
    par = sum(x[::2])
    last = x[-1]
    res = last * par
    print(res)