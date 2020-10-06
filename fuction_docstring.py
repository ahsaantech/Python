def function1():
    """This is test only --doc--"""
    print("Hellow you are in function 1")   #no print
function1()  # Print hellow you are in function1


def function2(a,b):
    print("This fuction2 add two number ",a+b)
function2(7,5)

def function3(a,b):
    """This is a function which will calculate
      average of two numbers
      this function doen't work for three number"""
    average=(a+b)/2
    print(average)
    return average
v=function3(12,16)
print(v)

print(function1.__doc__)
print("\n")
print(function3.__doc__)



