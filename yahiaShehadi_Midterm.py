# #main page of the system
# #resourses w3schools.com
# set the admin
correctUserName = "admin"
correctPassword = "admin123123"
from datetime import datetime
# # create time and date stamps
now = str(datetime.now())
dateOnly = now.split(" ", 1)
print(dateOnly[0])  #date
print(now)  #date and time

count = 0
userName = "incorrect"
password = "incorrect"


#this function to diaplay statistics num==1
def displayStatistics():
  male = 0
  female = 0
  with open('data.txt') as f:
    for x in f:
      a = x.split()
      # print(a[3])
      if a[3] == "male,":
        male += 1
      else:
        female += 1

  print("in our company we have", male, "men, and ", female, "ladies")


# this function to add new employee num==2
def addEmployee():
  c = 0
  with open('data.txt', 'r') as f:  #generate employee ID
    for line in f:
      c += 1
    empId = "emp"
    if c < 10:
      empId += ("00" + str(c))
    elif c > 10 and c < 100:
      empId += "0" + str(c)
    elif c > 100:
      empId += str(c)
    asd = empId
    f.close()
  name = input("enter employee's name : ")
  gender = input("enter employee's gender : ")
  salary = int(input("enter employee salary : "))
  f = open("data.txt", "a")
  f.write("\n" + empId + ", " + name + ", " + dateOnly[0] + ", " + gender +
          ", " + str(salary))
  print(asd, name, dateOnly[0], gender, salary)




while count < 5 and (userName != correctUserName
                     or password != correctPassword):
  # insertUserName()
  userName = input("enter username : ")
  password = input("enter password : ")
  if userName != correctUserName or password != correctPassword:
    count += 1
  elif userName == correctUserName and password == correctPassword:
    print("welcome Admin")
    print("1. Display Statistics")
    print("2. Add an Employee")
    print("3. Display all Employees")
    print("4. Change Employee’s Salary")
    print("5. Remove Employee")
    print("6. Raise Employee’s Salary")
    print("7. Exit")
    num = int(input("Please enter your choise:  "))
    if num == 1:
      displayStatistics()

    elif num == 2:
      addEmployee()
    elif num == 3:
      with open("data.txt","r") as f:
        print(f.read())
        
    elif num == 4:
      with open("data.txt", "r") as f:
        theID = input("enter employee ID to change the salary: ")
        theId = theID+","
        for i in f:
          a = i.split()
          if theId == a[0]:
            newSalary= input("enter the new salary: ")
#     https://pythonexamples.org/python-replace-string-in-file/       
            fin = open("data.txt", "rt")
            data = fin.read()
            data = data.replace(a[4], newSalary)
            fin.close()
            fin = open("data.txt", "wt")
            fin.write(data)
            fin.close()
    elif num == 5:
      with open("data.txt", "r") as f:
        theID = input("enter the ID to remove the employee: ")
        theId = theID+","
        for i in f:
          a = i.split()
          if theId == a[0]:
#     https://pythonexamples.org/python-replace-string-in-file/                 
            print(a[1]," is removed")
            fin = open("data.txt", "rt")
            data = fin.read()
            data = data.replace(i, "")
            fin.close()
            fin = open("data.txt", "wt")
            fin.write(data)
            fin.close()
    elif num== 6 :
      with open("data.txt", "r") as f:
        theID = input("enter the ID to raise the salary of an employee: ")
        theId = theID+","
        for i in f:
          a = i.split()
          if theId == a[0]:
#     https://pythonexamples.org/python-replace-string-in-file/                 
            rParcent=float(input("enter raise percentage: "))
            x = float(a[4])
            newSalary= x*rParcent
            fin = open("data.txt", "rt")
            data = fin.read()
            data = data.replace(a[4], str(newSalary))
            fin.close()
            fin = open("data.txt", "wt")
            fin.write(data)
            fin.close()
    elif num== 7:
      break  
      
      
            

