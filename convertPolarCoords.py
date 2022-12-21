######################################################################################
#   EXAMPLE 2.2: CONVERTING POLAR COORDINATES                                        #
#   Suppose the position of a point in two-dimensional space is given to us in polar #
#   coordinates r, θ and we want to convert it to Cartesian coordinates x, y.        #
######################################################################################

from math import sin, cos

def convertPolarToCartesian(r, theta):
    x = r*cos(theta)
    y = r*sin(theta)
    x = round(x, 2)
    y = round(y, 2)
    cartesianStr = ("x = " + str(x) + "\n" + "y = " + str(y))
    return cartesianStr


def main():
    
    r = float(input("Please enter your value for radius(r): "))
    theta = float(input("Please enter your value for the angle(in degrees): "))

    print(convertPolarToCartesian(r, theta))

if __name__ == "__main__":
    main()