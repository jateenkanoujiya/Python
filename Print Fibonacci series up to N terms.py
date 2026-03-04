a=int(input("Enter a number to print Fibonacci series up to: "))
a1=0
a2=1
if a<=0:
    print("Please enter a positive integer")
elif a==1:  
    print("Fibonacci sequence up to",a,":")
    print(a1)
else:
    print("Fibonacci sequence up to",a,":")
    print(a1)
    print(a2)
    for i in range(2,a):
        a3=a1+a2
        print(a3)
        a1=a2
        a2=a3
