#Multiple Variable Assignment
a = b = c = 3
#Introducing Dictionary.
a,b,c = ["C","Kon","Choc"]
print(a,b,c)

#Fixing Unpacking
a,_,b,c = ["C","Kon","Choc","Tex"]
print(a,b,c)

#Fixing Unpacking2
a,b,*c = ["C","Kon","Choc","Tex",200,400,200]
print(a,b,c)