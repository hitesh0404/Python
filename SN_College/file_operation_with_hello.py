# f = open("hello.txt")
# data = f.read()
# print(data)
# f.close()

# with open("hello.txt","r+") as f1:
#     print(f1.read())
#     print(f1.write("Hey its me Hitesh"))
#     f1.seek(0,0)
#     print(f1.read())


num=2
with open("table.txt","w") as f:
    for i in range(1,11,1):
        f.write(f"{num} X {i} = {num*i}\n")
