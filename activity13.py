# Input
# Age (Integer)
# is_employed (boolen)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolen)
 

age = int(input(" input age "))
is_employed = bool(input("Are you currently employed (True/False)  "))
credit_score = int(input("Credit score"))
annual_income = float(input("what is your annual income "))
has_collateral = bool(input("Do you have any collateral"))

if age >= 21 and is_employed == True:
    print("Passed baseline eligibility")

else:
    print("Rejected, failed baseline eligibility")

    #Tier 1 : High Credit (credit_score >= 750)
    # Base interest rate: 5.0%
    # If annual_income >= 100,000 give a loyalty discount
    if credit_score >= 750:
        if annual_income >= 100000:
           base_rate = 4.5
           print("Hi your interest rate is ", base_rate)
    else :
       print("Rejected, failed baseline eligibility")

       if annual_income >= 100000:
           print("You have a high Annual income")
           base_rate = 4.5
           print("Hi Your interest rate is ", base_rate)

     
