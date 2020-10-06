list =["harry","larry","carry","marry"]
print(list[0],list[1],list[2])
for item in list:
    print(item)

list1=[["harry",1],["larry",5],["carry",6],["marry",4]]
for item in list1:
    print(item)

# for item, lollypop in list1:
#     print(item,lollypop)
#
#     print(item,"and lolly is", lollypop)

dict1=dict(list1)
print(dict1)
for item, loyypop in dict1.items():
    print(item, "and lolly is",loyypop)

for item in dict1:
    print(item)


# Quiz:-
# find a number in list less then 6

items=[int, float, "harry", 5,2,6,8,9,2,4,5]
for item in items:
    if str(item).isnumeric() and item<6:
        print(item)
