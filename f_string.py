import math

# string formatting  today formatting not use
me="harry"
a="this is %s" %me
print(a)

me="harry"
a1=3
b="This is %s %s" %(me,a1)
print(b)

me= "harry"
a2=3
c="this is {} {}"
d=c.format(me,a2)
print(d)


# f string

mm="harry"
q=3
w=f"this is {mm} {q} {math.cos(65)}"  #import math use
print(w)
