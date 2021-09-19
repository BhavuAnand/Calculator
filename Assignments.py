print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

option=int(input("Enter choice from 1-4:")

if option==1:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a+b
    print("The sum is = ",c)
    
elif option==2:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a-b
    print("The difference is = ",c)
    
elif option==3:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a*b
    print("The product is = ",c)

elif option==4:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a/b
    print("The quotient is = ",c)
else:
    print("The choice is invalid!")
