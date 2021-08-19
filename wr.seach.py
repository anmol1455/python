#file=open("search.txt","w")
#print("enter 10 name")
#x=1
#while(x<=10):
 #   string=input()
  #  file.write(string)
   # file.write("\n")
    #x=x+1
#file.close()

files=open("search.txt","r")
name=input("enter name which you want to search")
data=files.read().split()
iterator=iter(data)
name_iter=iter(name)

for x in range(0,len(data)):
    iter_next=next(iterator)
    iter2=iter(iter_next)
    for z in iter(iter2):
        iter3=next(iter2)
        print(z)
    #print(iter_next)
    #for char in iter(name):
        #print(char)
     #   if char==iter_next:
      #      print(iter_next,'match')
    #else:
       # print("no match found")
files.close()
