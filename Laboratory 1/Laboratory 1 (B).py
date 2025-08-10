import math
import sys

print(
"""
 _____________________________
| POLYGON AND AREA CALCULATOR |
|_____________________________|""")
class polygon():
    def __init__(self, no_sides, area):
        #self.name = name
        self.no_sides = no_sides
        self.area = (math.pi/4) * side**2 * (1/math.tan(math.radians(180/self.no_sides)))
        
    def polygon_name(self):
        if self.no_sides < 3:
            print("\nIt is not polygon.")
        elif self.no_sides == 3:
            print("\nName of the Polygon: Triangle")
        elif self.no_sides ==4:
            print("\nName of the Polygon: Square")
        elif self.no_sides == 5:
            print("\nName of the Polygon: Pentagon")
        elif self.no_sides == 6:
            print("\nName of the Polyon: Hexagon")
        elif self.no_sides == 7:
            print("\nName of the Polygon: Heptagon")
        elif self.no_sides == 8:
            print("\nName of the Polygon: Octagon")
        elif self.no_sides == 9:
            print("\nName of the Polygon: Nonagon")
        elif self.no_sides == 10:
            print("\nName of the Polygon: Decagon")
        else:
            print(f"\nName of the Polygon: {self.no_sides} sides polygon")
    
    def Area(self):
        print(f"Number of Sides:       {self.no_sides}")
        print(f"The Area of a polygon: {self.area:.2f}")
        print("-"*30)
                        

no_sides = int(input("\nEnter Number of Sides: "))
if no_sides >= 3: 
    side = float(input("Enter Length of 1 side: "))
    shape = polygon(no_sides, side)
    shape.polygon_name()
    shape.Area()
else:
    print("It is not a polygon.")
    sys.exit