passengers = ['Rahul Sharma','Priya Patel','Amit Verma']

print("Passenger Reservation List: ",passengers)

print("\nFirst Passenger:  ",passengers[0])

print("\nSecond Passenger: ",passengers[1])

print(" \nThird Passenger: ",passengers[2])

passengers.append("Sneha Joshi")

print(passengers)

passengers.remove("Amit Verma")

print(passengers)

passengers.insert(1,"Rohan Mehata")

passengers.pop(2)

print(passengers)

print("Updated Reservation List: ")
print(passengers)