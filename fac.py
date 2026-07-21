num=int(input("enter any number::"))
def fac(num):
    if num==1 or num==0:
       return 1
    elif num<0:
       print("factorial of given number not define")
    else:
       return num*fac(num-1)
       
print("factorial of given number is::",fac(num))
