import re
string="i am, anmol, singh and i study btech 2018 batch"
#out=re.findall("[aei]",string)#a i and e in whole string
#out=re.findall("[a-h]",string)#a to h in whole string
#out=re.findall("[a-hA-H]",string)#a to h and A to H in whole string
#out=re.findall("\d",string)#digits in whole string
#out=re.findall("[0-9]",string)#0 to 9 in whole string
#out=re.findall("\s",string)#spaces in whole string
#out=re.findall("\S",string)#non space in whole string
#out=re.findall("^i am",string)#starts with i am in whole string
#out=re.findall("batch$",string)#ends with batch in whole string
#out=re.findall("^i am..batch$",string)#starts with i a and ends with batch in whole string
#out=re.findall("si..h",string)#starts with si and ends with h and have 2 characters in beteen in whole string
#out=re.findall("[^ei]",string)#words except e and i in whole string
#out=re.findall("\D",string)#no digits in whole string
#out=re.findall("\W",string)#no words in whole string
#out=re.findall("\w",string)#words in whole string
#out=re.findall("batch\Z",string)#ends with in last in whole string
#out=re.findall(r"\banmol\b",string)#do same as z but for every word in whole string

print(out)
if(out):
    print("exists")
else:
    print("not exists")
