m1=int(input("enter a marks of first subject::"))
m2=int(input("enter a marks of Second ubject::"))
m3=int(input("enter a marks of Third subject::"))
m4=int(input("enter a marks of forth subject::"))
m5=int(input("enter a marks of fifth subject::"))
total_marks=m1+m2+m3+m4+m5
percentage=(total_marks*100)/500
print("percentage",percentage,"%")

if percentage>=75 and percentage<=100:
   print("DISTINGTION")
elif percentage>=65:
   print("SECONG CLASS")
elif percentage>=40:
   print("FIRST CLASS")
else:
   print("SORRY....YOU ARE FAIL")
