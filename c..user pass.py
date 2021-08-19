class user_passwd:
    def register(self):
        file=open("login.txt","a")
        user=input("input username")
        file.write(user)
        file.write("\n")
        file2=open("login2.txt","a")
        passwd=input("input passward")
        file2.write("\n")
        file2.write(passwd)
        

    def login(self):
        user=input("input user name")
        file=open("login.txt","r")
        data=file.read().split()
        file2=open("login2.txt","r")
        data2=file2.read().split()
        print(data)
        print(data2)

        for y in range(len(data)):
            #print(data[y])
            if(user==data[y]):
                    passw=input("enter passward")
                    for z in range(len(data2)):
                        
                        if(passw==data2[z]):
                            print("yor are login")
                        #else:
                             #print("account blocked")
                    #break           
            #else:
               # print()
        file.close()
        file2.close()



user=user_passwd()
print("fill detail for registration")
user.register()
print("fill detail for login")
user.login()
