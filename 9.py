lower,upper=map(int,raw_input().split())
count=0
for z in range(lower,upper+1):
    if z>1:
        for x in range(2,z):
            if(z%x)==0:
                break
        else:
            count=count+1
print count         
