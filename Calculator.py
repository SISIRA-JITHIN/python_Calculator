x="yes"
while (x=="yes"):
    a=int(input("Enter the first number : "))
    b=int(input("Enter the seccond number : "))
    s=input("Enter the operation (Select anyone +,-,/,*,%) : ")
    if s=="+":
       c=(a+b)
       print("Addition result : ",c)
    elif s=="-":
        d=(a-b)
        print("Sutraction result : ",d)
    elif s=="*":
        e=(a*b)
        print("Multiplication result : ",e)
    elif s=="/":
        f=(a/b)
        print("Division result : ",f)
    elif s=="%":
        g=(a%b)
        print("Percentage result : ",g)
    else:
        print(" invalid input")

    x=input("Do you want to continue yes/no : ")
