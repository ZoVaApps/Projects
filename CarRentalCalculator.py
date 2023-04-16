#Colson Stewart
#HW06

#Declare variables and constants
CN = "?"
CT = "?"
DR = "?"
totalCharge = 0

Base_Fee = 65
Standard_Fee = 10
SUV_Fee = 15
Van_Fee = 25

#User Input
CN = input("What is you name: ")
CT = input("What type of car is it(Compact, Standard, SUV, Van): ")
DR = int(input("How many days do you wish to rent: "))

#Determine total charge

if CT == "Compact":
    totalCharge += Base_Fee
if CT == "Standard":
    totalCharge += Standard_Fee + Base_Fee
if CT == "SUV":
    totalCharge += SUV_Fee + Base_Fee
if CT == "Van":
    totalCharge += Van_Fee + Base_Fee
if DR >= 8:
    totalCharge = totalCharge - (totalCharge * .20)
else:
    totalCharge = totalCharge


    
#Ouput
print("Customers Name: ",CN)
print("Customers Car Type: ",CT)
print("Customers Days of Rental: ",DR)
print("Customers Total Charge: ",totalCharge)
    
    

    



