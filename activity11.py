#import demo
import getpass #folder


username = "JP"
password = "MANTIS"

u = input("input USERNAME ---> ")
p = getpass.getpass("input PASSWORD ---> ")

if u == username or  p  == password:
        print("username  and password correct")

else:
        print(" access denied")

