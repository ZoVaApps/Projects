# initialize the list of classes
classes = ["Pickle Ball", "Water Aerobics", "Kid Yoga", "Prenatal Yoga", "Silver Sneakers"]

# initialize the list of class requests
requests = [0, 0, 0, 0, 0]

# prompt the user to enter a class number and increment the corresponding request count
while True:
    class_num = int(input("Enter a class number (1-5) or 0 to exit: "))
    if class_num == 0:
        break
    requests[class_num-1] += 1

# display the number of requests for each class
for i in range(5):
    print(f"Class {i+1}: {classes[i]} - {requests[i]} requests")
