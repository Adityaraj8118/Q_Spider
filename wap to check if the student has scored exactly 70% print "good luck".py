#wap to check if the student has scored exactly 70% print "good luck"
math=int(input("enter math marks:- "))
py=int(input("enter math py:- "))
eng=int(input("enter math eng:- "))
java=int(input("enter math java:- "))

marks=math+py+eng+java
print(marks)

per=marks/400*100
print(per)
if per==70:
    print("Good luck")
