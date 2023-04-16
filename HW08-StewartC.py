#Colson Stewart
#HW08

#Constants and Variables
tuition = 5000  
year = 1  

#Output/Calculation
print("Year\t Tuition")  

while year <= 10:
    print(year,"\t$", tuition, sep="")  
    tuition *= 1.03  
    year += 1  