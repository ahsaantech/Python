# f=open("test3.text","w")
# f.write("New line print")
# f.close()

# f=open("test3.text","a")
# f.write("New line print\n")
# f.close()

# f=open("test3.text","a")
# a=f.write("New line ")
# print(a)
# f.close()

f=open("test3.text","r+")
print(f.read())
f.write("Thank you") #no out but add massage file
f.close()

