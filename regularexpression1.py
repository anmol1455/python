import re
s=" i am anmol and amit pool"
o=re.findall(r"\bam",s)
print(o)
e=re.findall(r"ol\b",s)
print(e)
ss=re.sub("a","8",s)
print(ss)
se=re.split(" ",s,3)
print(se)
if(re.search(r"ol\b",s)):
   print("exists")
else:
    print("doesn't exists")
