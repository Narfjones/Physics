#    Exercise 2.1: Another ball dropped from a tower
#    A ball is again dropped from a tower of height h with initial velocity zero. Write a
#    program that asks the user to enter the height in meters of the tower and then calculates
#    and prints the time the ball takes until it hits the ground, ignoring air resistance. Use
#    your program to calculate the time for a ball dropped from a 100 m high tower.
##################################################################################################################################################

from math import sqrt

def main():

    height = int(input("Please input the height from which the ball is dropped: "))
    print("It will take the ball " + str(DropCalculator(height)) + " seconds to get to the ground.")



def DropCalculator(height):

    dropTime = sqrt(2*height/9.81)
    dropTime = round(dropTime, 2)

    return dropTime

if __name__ == "__main__":
    main()