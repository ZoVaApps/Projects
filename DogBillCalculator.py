#Colson Stewart
#HW07

#Constants and Variables
Total_bill = 0
Dog_Name = "?"
Owner_Name = "?"
Breed = "?"
Age = "?"
Weight = "?"

fee = 0
#User Input
Dog_Name = ("What is the dogs name: ")
Owner_Name = ("What is your name: ")
Breed = input("What is the dogs breed: ")
Age = int(input("How old is the dog: "))
Weight = int(input("How much does the dog weigh: "))

#Determine Charge
if Weight < 15:
    fee = 55
if 15 <= Weight < 31:
    fee = 75
if 31 <= Weight < 81:
    fee = 105
if Weight >= 81:
    fee = 125



#Output
print("Bill")
print("Dogs Name: ",Dog_Name)
print("Owners Name: ",Owner_Name)
print("Dogs Breed: ",Breed)
print("Dogs Age: ",Age)
print("Dogs Weight: ",Weight)
print("Total Charge: ",fee)




