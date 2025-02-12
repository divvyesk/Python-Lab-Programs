#Experiment No 3: Control Statements, Loops and Functions
#Roll no: 2403080
#Name: Divvye Kansara
#Date: 12th Feb, 2025

#EXP 3 A): write a python program to take a numerical input and identify whether it is even or odd, utilizing condtional statements and loops
'''
c= input("Do you want to start(/continue)? Enter Y for yes and N for no: ")

while c != "N":
    x= int(input("Enter a number: "))

    if(x%2 == 0):
        print("It is an even number!")

    else:
        print("It is an odd number!")

    c= input("Do you want to start(/continue)? Enter Y for yes and N for no: ")



#EXP 3 B): write a python program to compute the factorial of a given integer N

a = int(input("Enter a number: "))
fact=1;

while(a>0):
    fact *= a
    a-=1

print("The factorial is: ", fact)
    

#EXP 3 C): using function, write a python program to analyze the input number is prime or not

def prime(n):
    x=1
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            x=0
            break

        else:
            x=1
            break
        
    return x

b= int(input("Enter a number: "))

d= prime(b)

if(d==0):
    print("The given number is not prime!")
else:
    print("The given number is prime!")

#EXP 3 D): Write a python program to implement a simple calculator that takes user input and performs basic arithmetic operations(addition, subtraction, multiplication, division)
#using functions

def addition(e,f):
    return e+f

def subtraction(e,f):
    return e-f

def multiplication(e,f):
    return e*f

def division(e,f):
    return e/f

def modulus(e,f):
    return e%f

e=int(input("Input a number: "))
f=int(input("Input a number: "))

while(1):
    choice= int(input("Choose the operation\n 1. Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exit the program"))

    if(choice == 1):
        g=addition(e,f)
        print("Addition: ",g)
        
    elif(choice == 2):
        g= subtraction(e,f)
        print("Subtraction: ",g)

    elif(choice == 3):
        g= multiplication(e,f)
        print("Multiplication: ",g)

    elif(choice == 4):
        g= division(e,f)
        print("Division: ",g)

    elif(choice == 5):
        g= subtraction(e,f)
        print("Modulus: ",g)

    else:
        exit()
'''

#EXP 3 E): Write a python program to print a triangle pattern, emphasizing the transition from C to python syntax:

row= int(input("Enter the numbers of rows: "))

for i in range(0,row):
        for j in range(0, i):
            print("*",end="")
        print("")
        



