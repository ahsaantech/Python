d1={}    #  dictionary
print(type(d1))

d2={"harry":"burger",
    "rohan":"fish",
    "mohan":"roti"}
print(d2)
print(d2["harry"])

d3={"harry":"burger",
    "rohan":"fish",
    "mohan":"roti",
    "shubham":{"b":"maggi","l":"roti","d":"chicken"}}
print(d3)
print(d3["shubham"])
d3["ankit"]="junk food"
print(d3)
d3[45]="apply"
print(d3)
del d3[45]
print(d3)

d9=d2.copy()  # d9 is create dictionary
del d9["harry"]
print(d2)   # d2 dictionary list harry name not delete
print(d9)  # d9 harry deleted

print(d2.get("harry"))
d2.update({"leena":"toffee"})
print(d2)
print(d2.keys())
print(d2.items())
print("\n")




#Quiz

dic1={"a":"apple",
      "b":"ball",
      "c":"cat",
      "d":"dog",
      "e":"elephant",
      "f":"fish"}
a=str(input("Enter any word\t"))
print(dic1[a])









