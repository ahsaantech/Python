def add(a,b):
    return a+b
print(add(4,7))
c=add(5,7)
print(c)

minus=lambda x,y:x-y
def minu(x,y):
    return x-y
print(min(8,4))
print(minus(9,4))

def a_first(d):
    return d[1]
d=[[1,14],[5,6],[8,23]]
d.sort(key=a_first)
print(d)

e=[[1,14],[5,6],[8,23]]
e.sort(key=lambda x:x[1])
print(e)

