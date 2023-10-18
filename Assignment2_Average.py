
Name=(input("Enter Name:"))
Family=(input("Enter Family:"))

a=int(input("Enter Score 1:"))
b=int(input("Enter Score 2:"))
c=int(input("Enter Score 3:"))

Average=(a+b+c)/3

if(Average>=17):
    print(Name,Family," is Great")
elif(Average<17 and Average>=12):
    print(Name,Family,"is Normal")
else:
    print(Name,Family,"is Fail")
