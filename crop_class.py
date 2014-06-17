import random

class Crop:
    """A Generic food crop"""

    def __init__(self, growth_rate, light_need, water_need):
        #set the attributes with an initial value
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        # use an underscore to indicate if it is private

    def needs(self):
        #return a dictionary containng the light and water needs.
        return{"light need":self._light_need, "water_need":self._water_need}

    def report(self):
        #return a dictionary containg the type, status, growth and days growing
        return{"Type":self._type, "Status":self._status, "Growth":self._growth, "Days Growing":self._days_growing}

    def update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = 'Mature'
        elif self._growth > 5:
            self._status = 'Young'
        elif self._growth > 0:
            self._status = 'Seedling'
        elif self._growth == 0:
            self._status = 'Seed'
        

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self.update_status()

def auto_grow(crop, days):
    #grow the crop
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
    #getting light and water values
    Valid = False
    while not Valid:
        try:
            light = int(input("Enter light (1-10):"))
            if light >= 1 and light <= 10:
                Valid = True
            else:
                print("Not a valid value. Please enter a valid value")
        except ValueError:
            print("Not a valid value. Please enter a valid value")
    Valid = False
    while not Valid:
        try:
            water = int(input("Enter Water (1-10):"))
            if water >= 1 and water <= 10:
                Valid = True
        except ValueError:
            print("Not a valid value. Please enter a valid value")
    crop.grow(light,water)
                        
def display_menu():
    print("1. Grow Manually Over 1 Day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit Program")
    print()
    print("Please enter an option form the list above.")

def get_menu_choice():
    valid_option = False
    while not valid_option:
        try:
            Choice = int(input(""))
            if Choice >= 0 and Choice <= 3:
                valid_option = True
            else:
                print("That is not a valid chocie")   
        except ValueError:
            print("That is not a valid choice")
    print()
    return Choice

def manage_crop(crop):
    print("-----------------CROP MANAGEMENT PROGRAM-----------------")
    print("\n" * 2)
    Exit = False
    while not Exit:
        display_menu()
        option = get_menu_choice()
        if option == 1:
            manual_grow(crop)
        if option == 2:
            auto_grow(crop, 30)
        if option == 3:
            print(crop.report())
        elif option == 0:
            Exit = True
        print()
    print("BYE!")
            
        
    
                         
                         
          
        
def main():
    #instanciate the class
    new_crop = Crop(1,4,3)
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
