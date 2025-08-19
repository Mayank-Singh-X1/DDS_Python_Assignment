class CarNode:
    def __init__(self, plate):
        self.plate = plate
        self.next = None

class ParkingLot:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.head = None
        self.history = []

    def park_car(self, plate):
        if self.count >= self.size:
            print("Parking Lot FULL!")
            return
        node = CarNode(plate)
        node.next = self.head
        self.head = node
        self.count += 1
        print(f"Car {plate} parked.")

    def exit_car(self, plate):
        prev = None
        curr = self.head
        while curr:
            if curr.plate == plate:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                self.count -= 1
                self.history.append(plate)
                print(f"Car {plate} exited.")
                return
            prev = curr
            curr = curr.next
        print(f"Car {plate} not found.")

    def list_cars(self):
        curr = self.head
        print("\nCurrently Parked Cars:")
        while curr:
            print(f"- {curr.plate}")
            curr = curr.next

    def show_history(self):
        print("\nParking History:")
        for p in self.history:
            print(f"- {p}")

def main():
    lot = ParkingLot(size=5)
    while True:
        print("\n1. Park Car\n2. Exit Car\n3. List Parked Cars\n4. Parking History\n5. Exit")
        ch = input("Choice: ")
        if ch == "1":
            plate = input("Car plate number: ")
            lot.park_car(plate)
        elif ch == "2":
            plate = input("Remove plate number: ")
            lot.exit_car(plate)
        elif ch == "3":
            lot.list_cars()
        elif ch == "4":
            lot.show_history()
        elif ch == "5":
            break

if __name__ == "__main__":
    main()
