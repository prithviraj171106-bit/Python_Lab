def greet(name):
    print("Hello,", name)
greet("Alice")

"""Task 1: Create Function Using Default Arguments
    Define reservation function"""

def reservation_status(
   passenger_name,
   ticket_status="Confirmed"):
   print("Passenger Name :", passenger_name)
   print("Ticket Status :", ticket_status)

""" call The function"""

reservation_status("Rahul Sharma")
reservation_status("Amit Verma", "Waiting")


# Task 2: Use *args (Variable Length Arguments)

# 1 Create a function to handle multiple passenger names

def passenger_booking(*passengers):
   print("Passenger List:")
   for name in passengers:
       print("Passenger :", name)


# 2 Call the function with multiple variables



passenger_booking(
   "Rahul Sharma",
   "Priya Singh",
   "Amit Verma",
   "Neha Kapoor")


# Task 3: Use **kwargs (Keyword Variable Arguments)

# Create a function to store passenger ticket details dynamically

def ticket_details(**details):
   print("Ticket Information:")
   for key, value in details.items():
       print(key, ":", value)

# Call the function.

ticket_details(
   passenger_name="Rahul Sharma",
   train_name="Rajdhani Express",
   seat_number="B1-21",
   fare=2500,
   status="Confirmed")

# Task 4: Create Recursive Seat Countdown Function.

# Define recursive function

def seat_countdown(seats):
   if seats == 0:
       print("All Seats Booked")
       return
   print("Remaining Seats :", seats)
   seat_countdown(seats - 1)

# Call the recursive function.

seat_countdown(5)

# Task 5: Create Recursive Passenger Verification Function.

# Define recursive verification function.

def verify_passenger(passenger_number):
   if passenger_number == 0:
       print("Verification Completed")
       return
   print("Verifying Passenger :", passenger_number)
   verify_passenger(passenger_number - 1)

# Call the function.

verify_passenger(3)

# Task 6: Build Final Advanced Booking Module.

# Create final booking function.

def final_booking(
   train_name="Rajdhani Express",
   *seat_numbers
):
   print("===================================")
   print(" Railway Reservation ")
   print("===================================")
   print("Train Name :", train_name)
   for seat in seat_numbers:
       print("Allocated Seat :", seat)

# Call the function

final_booking(
   "Rajdhani Express",
   "B1-21",
   "B1-22",
   "B1-23")

