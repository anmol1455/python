file=open("user1.txt","w")
user=input("enter user name")
passward=input("enter passward")
file.write(user)
file.write("\n")
file.write(passward)
file.write("\n")
print("data inserted")
file.close()
