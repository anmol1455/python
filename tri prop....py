angle1=int(input("enter first angle"))
angle2=int(input("enter second angle"))
angle3=int(input("enter third angle"))
if(angle1+angle2+angle3==180 and angle1>0 and angle2>0 and angle3>0):
    if(angle1<90 and angle2<90 and angle3<90):
        print("acute angle triangle")
    elif(angle1>90 or angle2>90 or angle3>90):
        print("obtuse angle triangle")
    else:
        print("right angle triangle")
else:
    print("enter correct angle")
