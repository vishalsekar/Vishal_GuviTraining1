class uberride:
    def __init__(self,distance,vehicle):
         self.distance=distance
         self.vehicle=vehicle
    
    def price_calculation(self):
         if self.vehicle == "bike":
              rate=10
         elif self.vehicle =="auto":
              rate=15
         elif self.vehicle =="car":
              rate=20
         else:
              print("Vehicle is not available")
              return 
         

         total=self.distance*rate
         print("Total fare: ",total)
 
distance=float(input("Enter the distance(km) : ")) 
vehicle=input("Enter the vehicle(bike/auto/car) : ")

ride=uberride(distance,vehicle)
ride.price_calculation()