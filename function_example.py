def a():
    a=int(input("Enter any number"))
    b=int(input("Enter any number"))
    c=a+b
    print(c)
    again()



def again():
    cal=input("Enter y for contunue and n for exit ")
    if cal=='y':
        a()
    elif cal=='n':
        print("See you later")
    else:
        print("Please enter y and n ")
        again()

a()


