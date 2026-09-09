#multiple if and elif condition

#create a python program that woud capture age group

name =input(" Please input your name ---> ")

age =int(input(" Please input your age ---> "))

if age >= 0 and age <=5 :
       print("that age is considered as INFANT ")

elif age >= 6 and age <=12 :
       print("that age is considered as kid ")

elif age >= 13 and age <=15 :
       print("that age is considered as pre - teen ")

elif age >= 16 and age <= 19 :
       print("that age is considered as Teenager ")

elif age >= 20 and age <= 29  :
       print("that age is considered as pre - Early Adulthod")

elif age >= 30 and age <= 58 :
       print("that age is considered as pre - Adult ")

elif age >= 60 and age <= 90 :
       print("that age is considered as pre - Senior ")

else:
     print("age invalid ")


