#Experiment No 1: Python Basic, Datatype, operator, input, output
#Roll no: 2403080
#Name: Divvye Kansara
#Date: 5th Feb, 2025

print("#EXP 1 A):  write a python code to generate a personalized greeting")
 
name = input("Enter your name: ")
print(f"Welcome to Python Programming {name}!")
 

print("\n#EXP 1 B): write a python code to calculate area of any geometric figure circle, rectangle and triangle")

 
shape = input("Enter R for rectangle, C for circle, and T for triangle: ")

if(shape == 'R'):
    a= int(input("Enter the length of the rectangle: "))
    b= int(input("Enter the breadth of the rectangle: "))
    arear= a*b
    print("Area of rectangle is: ", arear)

elif(shape == 'C'):
    r= int(input("Enter the radius of the circle: "))
    areac= 3.14*r*r
    print("Area of circle is: ", areac)

elif(shape == 'T'):
    h= int(input("Enter the height of the triangle: "))
    ba= int(input("Enter the breadth of the rectangle: "))
    areat= 0.5*h*ba
    print("Area of triangle is: ", areat)
    
else:
    print("Invalid choice try again!")
 

print("\n#EXP 1 C): Developing conversion inches to feet, inr to dollar, C to F")
 
inr = int(input("Enter rupees in INR: "))
dollar= inr*87
print("Value in Dollars: ", dollar)

inches= int(input("Enter length in inches: "))
feet= inches/12
print("Length in feet= ", feet)

celcius= int(input("Enter temperature in Celcius: "))
faren= (celcius*(9/5))+32
print("Temperature in Farenheit = ", faren)
 

print("\n#EXP 1 C): Write a program code to calculate the gross salary of an employee")
 
bsalary= int(input("Enter the basic salary: "))
da= 0.7*bsalary
ta= 0.3*bsalary
hra= 0.1*bsalary
gsalary= bsalary+da+ta+hra

print("Gross salary of the given employee:  ",gsalary)


print("\n#EXP 1 D): calculate simple interest")

pa= int(input("Enter Principal Amount: "))
t= int(input("Enter the time: "))
r= int(input("Enter the rate of interest: "))
si=(pa*r*t)/100
print("Simple interest: ", si)


print("\n#EXP 1 E): Write a python code to perform arithmetic operations addtion, subtraction, mutliplication, division and modulus")

a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
sum= a+b
print("Addition of a and b is: ", sum)

c=  int(input("Enter a number: "))
d= int(input("Enter a number: "))
sub=c-d
print("Subtraction of c and d is: ", sub)
       
e=  int(input("Enter a number: "))
f= int(input("Enter a number: "))
mul= e*f
print("Multiplication of e and f is: ", mul)      

g=  int(input("Enter a number: "))
h= int(input("Enter a number: "))
div= g/h
print("Division of g and h: ", div)

i=  int(input("Enter a number: "))
j= int(input("Enter a number: "))
mod= i%j
print("Modulus of i and j: ", mod)       
