class user_passwd:
    def register(self):
        file=open("login.txt","a")
        file2=open("login2.txt","a")
        user=input("input username")
        passwd=input("input passward")
        file.write(user)
        file.write("\n")
        file2.write(passwd)
        file2.write("\n")

        

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
           
        file.close()
        file2.close()



user=user_passwd()
print("fill detail for registration")
user.register()
print("fill detail for login")
user.login()
