import heapq
import random

class Driver:
    def __init__(self, name, distance, rating):
        self.name = name
        self.distance = distance
        self.rating = rating

    def __lt__(self, other):
        # For priority: closer, then higher rating
        return (self.distance, -self.rating) < (other.distance, -other.rating)

class Rider:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

drivers = []
ride_requests = []
ride_history = []

def add_driver():
    name = input("Driver name: ")
    distance = float(input("Distance (km): "))
    rating = float(input("Rating (0-5): "))
    heapq.heappush(drivers, Driver(name, distance, rating))

def new_ride_request():
    name = input("Rider name: ")
    destination = input("Destination: ")
    ride_requests.append(Rider(name, destination))

def assign_ride():
    if not drivers or not ride_requests:
        print("No available drivers or ride requests.")
        return
    rider = ride_requests.pop(0)
    driver = heapq.heappop(drivers)
    print(f"Assigned driver {driver.name} (distance {driver.distance}km, rating {driver.rating}) to {rider.name}.")
    ride_history.append({"rider": rider.name, "driver": driver.name, "destination": rider.destination})

def list_ride_history():
    print("\n--- Ride History ---")
    for ride in ride_history:
        print(f"{ride['rider']} -> {ride['destination']} with {ride['driver']}")

def main():
    while True:
        print("\n1. Add Driver\n2. New Ride Request\n3. Assign Ride\n4. Show Ride History\n5. Exit")
        ch = input("Choice: ")
        if ch == "1":
            add_driver()
        elif ch == "2":
            new_ride_request()
        elif ch == "3":
            assign_ride()
        elif ch == "4":
            list_ride_history()
        elif ch == "5":
            break

if __name__ == "__main__":
    main()
