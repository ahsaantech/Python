f = open("test.txt","rt")
content = f.read()
print(content)
f.close()

f = open("test2.txt","rt")
content = f.read(3)
print("1",content)
content=f.read(2)
print("2",content)
f.close()


f = open("test2.txt","r")
# content = f.read()
for line in f:
    print(line)
f.close()

f = open("test2.txt","r")
# print(f.readline())
# print(f.readline())
print(f.readlines())
f.close()
