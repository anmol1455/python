file=open("search.txt","r")
data=file.read().split()
iterator=iter(data)
print(iterator)
#for char in range(0,len(data)):
    #next_iter=next(iterator)
  #  print(char)
iterator2=iter(iterator)
for char2 in iter(iterator2):
            print(char2)


