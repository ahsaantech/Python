"""
()   tuple
[]   list
{}   dictionary
"""

grocery=["Harpic","vim bar","deodrant","Lollypop",57]
print(grocery)
print(grocery[1])
number=[2,8,1,6,9,4]
print(number)
number.sort()
print(number)
number.reverse()
print(number)

print(number[2])  # it's called salicing
print(number[0:6])
print(number[1:]) #index 0 is hide
print(number[2:]) #index 0 or 1 hide

print(number[::1])  #it's called extended
print(number[::2])
print(number[::-1])  # only use -1 it's work proper

print(max(number))
print(min(number))
number1=[]
number1.append(5)
number1.append(2)
number1.append(9)
print(number1)

number1.insert(0,34)  # 0 is index number
number1.insert(1,23)
print(number1)

number1.remove(23)  # remove choosen number
number1.pop()   # remove last number
print(number1)

number1[1]=98  # [1] is index
print(number1)

tp=(1,4,7)    #  tuple
print(tp)
print(type(tp))
tp1=(1)  # print not tuple
tp2=(1,)
print(tp1,tp2)


#  Mutable  =  Can change (list)
#  Immutable = cannot change (tuple)


a=5
b=8
a,b=b,a
print(a,b)