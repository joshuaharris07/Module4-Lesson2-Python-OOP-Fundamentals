# City Infrastructure Management System
# Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to 
# build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, 
# and data structures to manage different aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

# - Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

# Expected Outcome: Completion of the Vehicle class with the update_owner method and a 
# demonstration script showing the creation of Vehicle objects and updating their owners.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The owner of the {self.type} is now {new_owner}")
    
    def display_details(self):
        print(f"Registration Number: {self.registration_number}, Vehicle Type: {self.type}, Owner: {self.owner}")

vehicle1 = Vehicle("AAA111", "Honda Pilot", "John Doe")
vehicle2 = Vehicle("ABC123", "Ford Explorer", "Mike Smith")

vehicle1.display_details()
vehicle2.display_details()

new_owner1 = "Moby Dog"
vehicle1.update_owner(new_owner1)

new_owner2 = "Charlie Cat"
vehicle2.update_owner(new_owner2)

vehicle1.display_details()
vehicle2.display_details()


# Task 2: Event Management System Enhancement

# - Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
# Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
    
    def add_participant(self, change):
        self.participant_count += change

    def get_participant_count(self):
        print(f"The current participant count for the {self.name} is: {self.participant_count}")

name = "5k Fun Run"
date = "September 10th, 2025"
event1 = Event(name, date)

event1.get_participant_count()

register_participants = 56
event1.add_participant(register_participants)

event1.get_participant_count()