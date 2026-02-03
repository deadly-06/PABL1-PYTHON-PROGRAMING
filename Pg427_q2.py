x=int(input("enter x coordinates"))
y=int(input("enter y corrdinates"))
if x>0 and y>0:
    print("x and y lies in 1st quadrant")
elif x>0 and y<0:
    print("x and y lies in 4th quadrant")
elif x<0 and y>0:
    print("x and y lies in 2nd quadrant")
else:
    print("x and y lies in 3rd quadrant")
    
