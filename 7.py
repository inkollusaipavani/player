x=list(raw_input())
for i in range(0,len(x)-1,2):
    x[i],x[i+1]=x[i+1],x[i]
print("".join(str(k) for k in x))
