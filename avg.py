m1=int(input("enter first subject marks:"))
m2=int(input("enter second subject marks:"))
m3=int(input("enter third subject marks:"))
m4=int(input("enter forth subject marks:"))
m5=int(input("enter fifth subject marks:"))
avg=(m1+m2+m3+m4+m5)/5
print("average of the subjects is:",avg)
if avg>=90 and avg<100:
  print("first class")
elif avg>=70:
  print("second class")
elif avg>=50:
  print("distinction")
elif avg>=35:
  print("pass")
else:
  print("fail")
