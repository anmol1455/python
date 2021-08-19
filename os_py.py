import os
print(os.name)
print(os.getcwd())
os.chdir("C:\sikha")
print(os.getcwdb())
#os.mkdir("Anmol")
f=os.open("abc.txt",os.O_WRONLY | os.O_CREAT)
d="hjghfgh".encode('utf-8')
os.write(f,d)
os.close(f)





