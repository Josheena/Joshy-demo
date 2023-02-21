import random
class filter():
    
    def init(self):
        pass

    def location(self):
        loc,opt = obj_2.database(0,5)
        return loc,opt

    def room_type(self):
        room,opt = obj_2.database(5,10)
        return room,opt
        
    def rent_range(self):
        rent,opt = obj_2.database(10,15)
        return rent,opt

    def database(self,start,end):
        file = open("choice.txt","r")
        preference =file.readlines()
        for i in range(start,end):
            print(preference[i])
        output = int(input("Enter your option:"))
        return preference[start+output],output
        file.close()
        
print("-----FILTERS-----")
obj_2=filter()
Location , option_1= obj_2.location()
Type,option_2 = obj_2.room_type()
Rent,option_3 = obj_2.rent_range()
print("Your preferences are : ")
print(Location+Type+Rent )
