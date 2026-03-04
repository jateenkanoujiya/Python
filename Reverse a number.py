num=int(input("Enter a number to reverse: "))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print(f"Reversed number is: {reverse}")