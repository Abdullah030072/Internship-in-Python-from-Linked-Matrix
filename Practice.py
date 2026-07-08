#for printing the type of variable
num = 100
print (type(num))
##for print the number
print(num)
text ="ABDULLAH ABD"
#for print the first number of the string and string start from 0
#indexinng
print (text[1])
#slicing the string start is included but last is excluded
print(text[1:3])
#for reverse printing of string
print(text[::-1])
#for lower case
print(text.lower())
#for find any character from the overall string
print(text.find("H"))
#for replace any word from the overall string
print(text.replace("ABD","ABC"))
#for remove space from both ends
print(text.strip())
#for spliting the overall srting
print(text.split())
#for writing the text into title format
print(text.title())
#for first digit doing capital
print(text.capitalize())
#for upper case
print(text.upper())
#for finding the length of the string
print(len(text))
numbers = (10,20,30)
print(numbers)
print(numbers[1])
#This is comment;
#single word must be write in single or double commas
x='john'
print(x)
y="john"
print(y)
Age=39
print(Age)
age=35
print(age)
#assign the diferent valuse to different variables
x,y,z="Oraange","Banana","Cheery"
print (x)
print (y)
print (z)
#assign the same value to different variables
x =y =z ="BANANA"
print (x)
print (y)
print (z)
#unpack a collection
fruits = ["orange","banana","apple"]
x,y,z= fruits
print(x)
print(y)
print(z)
#for adding an item in the string using the append
fruits.append("new item  added")
print(fruits)
#function
x="awesome"
def myfun():
    print("Python is "+x)
myfun()
#global variable
def abc():
    global a
    a ="fantastic"
abc()
print ("python is "+a)
#python output variable 
#also  use the sign of + instead of comma 
 #but in + dont space added
#you dont add string into number  
#you show the string and number with the help of comma.  
q = "abc"
w = 'axbd'
e = 'buiv'
#for printing the string with the space
print (q,w,e)
#for print the string without space
print (q+w+e)  
#for printing the overall tuple 
number = (10,20,30)
print (number)
#for accesing value from the overall numbers
print (number[1])
#-----set----
#for showing the all set
#it ignores the double integers
num={1,2,3,4,2,5,6}
print (num)
#-----Dictionary------
student={
    "name":"ali","age":20,"city":"Lahore"
}
print(student)
#for accesing the value of variable
print(student["name"])
#for find the length of the string:
text="python"
print(len(text))
#-----Count ----
print(text.count("o"))
#----using the extend for adding the multiple items in the string
a= [1,2]
a.extend([3,4,5,6])
print(a)
#------inert function which is used for adding an item in a specific index
b=["ali","ahmad"]
b.insert(1,"usman")
print(b)
#----for remove the any number
abc =[1,3,4,5]
abc.remove(3)
print (abc)
#----pop function last wali value ko remove krta ha
d = [1,23,4,5,6,87]
d.pop()
print(d)
#----for clear the overall data from the variable
d.clear()
print(d)
#----for sorting the values
d = [1,23,4,5,6,87]
d.sort()
print(d)
#----for copy
a=[1,3,5,6,9]
b=a.copy()
print (b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)
print("Floor Division =", a // b)
print("Power =", a ** b)
