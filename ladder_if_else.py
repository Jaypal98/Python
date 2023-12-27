rno = int(input("Enter roll no of the student : "))
sname  = input("Enter name of the  student : ")
S1= int(input("Enter marks of subject 1 : "))
S2= int(input("Enter marks of subject 2 : "))
S3= int(input("Enter marks of subject 3 : "))

total = S1+S2+S3
per=total/3

print("Student name : ",sname)
print("Student name : ",rno)
print("Student name : ",total)
print("Percentage : ",per)


if per >= 70:
    print("Distinction")
elif per >=60:
    print("First class")
elif per>=50:
    print("second class")
elif per >=40:
    print("pass class")
else:
    print("fail")               