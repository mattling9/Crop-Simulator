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

    def __init__(self):
        #return a dictionary containng th light and water needs.
        

def main():
    #instanciate the class
    new_crop = Crop(1,4,3)
    print(new_crop._status)
    print(new_crop._light_need)
    print(new_crop._water_need)

if __name__ == "__main__":
    main()
