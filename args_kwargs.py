def funargs(normal,*args,**kwargs):
    # you are change *args and **kwargs name
    print(normal)
    for item in args:
        print(item)
        print("\n Now i would like to introduce some of our heros")
        for key, value in kwargs.items():
            print(f"{key} is a {value}")
har = ["harry","rohan","skill","hamad"]
normal="I am normal argument and the students are "
kw={"roshan":"monitor","harry":"fitness","shivam":"cook"}
funargs(normal,*har,**kw)
