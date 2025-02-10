#Experiment No 2: Python Data Structures
#Roll no: 2403080
#Name: Divvye Kansara
#Date: 5th Feb, 2025

print("EXP 2 A):  To manage a task list using list and tuples and perform add, remove, update and sort task\n");
task=[]

#adding a task
'''
task=["Go to the office", "pay the bills", "visit the doctor", "cook the food"]
add1=input("Add a task to append: ")
task.append(add1)
print("After appending: ", task)
task[2:3]= ["Go to the gym", "Go to the bank", "Order groceries"]
print(task)
add2=input("Add a task to append: ")
task.insert(1, add2)
print(task)
'''
task1=[]
for i in range(5):
  add3=input("Add a task: ")
  task1.append(add3)
 
print(task1)
 

#deleting a task
task1.pop()
print(task1)

del task1[1]
print(task1)

#sorting a task
task1.sort()
print(task1)

#view task
print(task1)

#list comprehension

task4 = [x for x in input("Enter the tasks sepearted by commas").split(",")]
print(task4)

#tuple as input from user

task5 = [x for x in input("Enter the tasks sepearted by commas").split(",")]
print(task5, type(task5))
task6=tuple(task5)
print(type(task6))

#sort tuple
print(sorted(task6))
print(sorted(task6, reverse=True))

#EXP 2 B):

cet_students= {"Divvye", "Jai", "Aaditya"}
jee_students= {"Darsh", "Pruthviraj", "Wilbert", "Aaditya"}
neet_students= {"Mohit", "Amaya", "Dhairya", "Aaditya"}

#union
union_students = cet_students | neet_students
print(union_students)

#intersection
intersection_students = cet_students & neet_students & jee_students
print(intersection_students)

#Difference (students in CET but not in NEET)
difference_students= cet_students- neet_students
print(difference_students)

#Difference (student in NEET but not in CET)
difference_students= neet_students- cet_students
print(difference_students)

#Symmetric Difference (student who are either in CET or NEET, but not both)
symmdiff_students= cet_students ^ neet_students
print(symmdiff_students)

#EXP 2 C): Write a python program to create, upload, and manipulate a dictionary of student records, including their grades and attendance

record1= {}
record2= {}

#adding students 
record1= {1:{'name': 'Amol', 'grades': [], 'attendance ':0}}
print(record1)
record1[2]= {'name': 'Nishit', 'grades': [], 'attendance ':0}
print(record1)
record1[3]={'name': 'Sagar', 'grades': [], 'attendance ':0}
print(record1)


