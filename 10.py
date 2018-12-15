s,x=map(str,raw_input().split())
c=0
for n in range(len(s)):
    if s[n]!=x[n]:
        c=c+1
if(c==1):
    print('yes')
else:
    print('no')
