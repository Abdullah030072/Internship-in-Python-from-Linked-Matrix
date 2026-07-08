#--------------if-else condition:-----------
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
number = int (input("Enter the number for checking it is even or odd :  "))
if number %2 == 0:
    print ("Even Number.")
else: 
    print("Odd Number.") 
#========if ..elif ...else Statements=======
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")
#===========Nested if else Conditions=========
age = int(input("Enter your age: "))
license = input("Do you have a driving license? (yes/no): ")
if age >= 18:
    if license == "yes":
        print("You can drive.")
    else:
        print("Get a driving license first.")
else:
    print("You are underage.")
   