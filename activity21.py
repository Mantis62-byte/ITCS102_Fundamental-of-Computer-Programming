#jeepney Simulator 
route = ["Terminal", "perez park", "pacific mall"]
passenger = []
SEATS = 6 
Fare = 13 
total = 0 

while True:
    print()
    print("Sakay", passenger)
    print(len(passenger) , "of", SEATS, "seats")
    print("1 sakay  2 Priority seats 3 para po!")
    print("4 baba sa pinto 5 baba sa harap")
    print("6 seat check 7 balikan 8 exit")
    choice = input("choice:  ")

    if choice == "1":
        if len(passenger) == SEATS:
            print("puno na! " )
        else:
            name = input|("Name: ")
            passenger.append(name)
            total = total + Fare
            print(name, "boarded at the back.")

    elif choice == "2":
        if len(passenger) == SEATS:
            print("puno na!")
        else:
            name = input("name: ")
            passenger.insert(0, name)
            total = total + Fare
            print(name, "tookl the priority seat.")

    elif choice == "3":
        name = input("who is getting off? ")
        if name in passenger:
            passenger.remove(name)
            print(name, "got off. ingat!")
        else:
            print(name, "is not on this jeep.")

    elif choice == "4":
        if len(passenger) == 0:
            print("The jeep is empty.")
        else:
            left = passenger.pop()
            print(left, "got off the door")

    elif choice == "5":
        if len(passenger) == 0:
            print("the jeep is empty")
        else:
            front = passenger.pop(0)
            print(front, "got off at the front")

    elif choice == "6":
        for i in range(len(passenger)):
            print("SEAT", i + i, passenger[i])

    elif choice == "7":
        route.reverse()
        print("Route:", route)

    elif choice == "8":
        print("total fare today:", total)
        break
    else:
        print("Invalid choice.")


