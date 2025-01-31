import math

def circle(radius):                #find area of circle
    print(" * Circle:\n")
    area=math.pi*(radius**2)
    print(f"Area of Circle : {area:.2f}")


def square(side):                  #find area of square
    print(" * Square:\n")
    area=side*side
    print(f"Area of Square :{area:.2f}")


def triangle(height,base):         #find area of triangle
    print(" * triangle:\n")
    area=(height*base)/2
    print(f"Area of triangle :{area:.2f}")


def rectangle(length,width):       #find area of rectangle
    print(" * Rectangle:\n")
    area=length*width
    print(f"Area of triangle :{area:.2f}")