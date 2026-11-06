tuloy = True 
while tuloy == True:
    ask = input("do you want to continue? (yes/no) --->")
    if ask.lower() == "yes":
        print("continue")
        continue
    else:
        print ("stop now")
        break