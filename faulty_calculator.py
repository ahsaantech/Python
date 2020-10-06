"""
Faulty Calculator
2+2=9
9-3=41
9*2=55
8/4=52
"""
number1=int(input("Enter first number :- "))
number2=int(input("Enter second number:- "))
print("Choose a operator :-")
print("+ Addition Operator")
print("- Subtraction Operator")
print("* Multiplication Operator")
print("/ Division Operator\n")
operator=input("Enter any one operator:-  ")
result=0
if number1==2 and number2==2 and operator=="+":
    result="9"
elif number1==9 and number2==3 and operator=="-":
    result="41"
elif number1==9 and number2==2 and operator=="*":
    result="55"
elif number1==8 and number2==4 and operator=="/":
    result="52"
elif operator=="+":
    result=number1+number2
elif operator=="-":
    result=number1-number2
elif operator=="*":
    result=number1*number2
elif operator=="/":
    result=number1/number2
else:
    result="You are wrong enter please check! "
print("\nYour result is :- ",result)



