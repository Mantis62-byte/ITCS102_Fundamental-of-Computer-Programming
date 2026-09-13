
sender = input("Enter Sender Name: ")
item = input("Enter Type of Item: ")

fragile_input = input("Is it fragile? (True/False): ")
if fragile_input == "True":
    fragile = True
else:
    fragile = False

weight = float(input("Enter Weight (kg): "))
distance = float(input("Enter Distance (km): "))

express_input = input("Is it express? (True/False): ")
if express_input == "True":
    express = True
else:
    express = False

international_input = input("Is it international? (True/False): ")
if international_input == "True":
    international = True
else:
    international = False

# Base Cost
cost = (weight * 2.50) + (distance * 0.15)

# Shipping Rates
if weight <= 2 and distance <= 100 and not express and not international:
    rate = "Free Shipping"
    total = 0

elif express and international:
    rate = "International Shipping"
    total = (cost * 1.40) + 50

elif express or (international and weight > 20):
    rate = "Heavy Shipping"
    total = (cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    rate = "Oversized Shipping"
    total = cost + 30

else:
    rate = "Standard Shipping"
    total = cost

print("\n---- Summary of the Item ----")
print("Sender Name:", sender)
print("Type of Item:", item)
print("Fragile:", fragile)
print("Shipping Rate:", rate)
print("Express:", express)
print("International:", international)
print("Total Shipping Cost: $", format(total, ".2f"))

