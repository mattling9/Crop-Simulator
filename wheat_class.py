from crop_class import *

class Wheat(Crop):
    """A Wheat Crop"""

    #constructor
    def __init__(self):
        super().__init__(1,3,6)
        self._type = "Wheat"
    def grow(self,light,water):
        if light >=self._light_need and water >= self._water_need:
            if self._status == "seedling" and water >= self._water_needed:
                growth = growth + growth_rate *1.5
            elif self._status == "Young" and water >= self._water_needed:
                growth = growth + growth_rate *1.25
            elif self._status == 'Old':
                self._growth = growth + growth_rate /2
            else:
                self._growth += self._growth_rate
                self._days_growing += 1
                self.update_status()
            
def main():
    wheat_crop = Wheat()
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == "__main__":
    main()
