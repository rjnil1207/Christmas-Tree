def fun(n):
    s = "Merry Christmas"

    for i in range(1,n+1,2):
        z = int((n-i)/2)
        print(" "*z , "*"*i)    # Printing the head of Tree

    z1 = max(5,n//4)
    z2 = int((n-z1)/2)
    for i in range(1,z2):
        print(" "*z2,"*"*z1)   # Print the Trunk of Tree

    t = int((n-len(s))/2)      # Print the String in Middle
    print(" "*t,s,"\n"*2)  

n = int(input("Enter the number(>15) :\n"))

if n%2 == 0:                   # Convert even to odd
    n = n-1
    fun(n)
else:                          # Number is odd
    fun(n) 
