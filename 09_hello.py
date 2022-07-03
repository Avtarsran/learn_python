class train:
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats
        self.fare = fare
    def getinfo(self):
        print(f"the name of the train is {self.name}")
        print(f"number of seats avaible is {self.seats}")
        print(f"price of tickets is {self.fare}")
    def booktickets(self):
        if self.seats>0:
            print(f'your seat has been booked {self.seats}')
            self.seats -= 1
        else:
            print('this train is fulled')

    def cancel(self,seatno):
        self.seats += 1
        print(f"{seatno} is cancelled seatno {self.seats} is now available")
      
g = train('rajdhani express',5,120)
g.getinfo()
g.booktickets()
g.booktickets()
g.booktickets()
g.booktickets()
g.booktickets()
g.cancel(5)
g.cancel(4)