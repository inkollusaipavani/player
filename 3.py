num1=int(raw_input())
reverse=0
while num1>0:
    digit=num1%10
    reverse=reverse*10+digit
    num1=num1//10
print reverse
