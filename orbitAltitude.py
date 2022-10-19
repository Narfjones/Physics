#    Exercise 2.2: Altitude of a satellite
#    A satellite is to be launched into a circular orbit around the Earth so that it orbits the
#    planet once every T seconds.

#    a) Show that the altitude h above the Earth’s surface that the satellite must have is h = ((GMT^2)/4π2)^1/3 − R,
#    where G = 6.67 × 10^−11 m^3*kg^−1*s^−2 is Newton’s gravitational constant, 
#    M = 5.97 × 10^24 kg is the mass of the Earth, and R = 6,371 km is its radius.
########################################################################################################################################################################
import math
import numpy

def altitudecalculator(period):
    bigG = 6.67*10**-11
    bigM = 5.97*10**24
    bigR = 6371*1000

    altitude = ((bigG*bigM*period**2)/(4*math.pi**2))**(1/3) - bigR
    altitude = round(altitude/1000, 2)

    return altitude

def problemA():
    print("Problem a solved in altitudecalculator function.")
    main()

##############################################################################################################################################
#    b) Write a program that asks the user to enter the desired value of T and then calculates and prints out the correct altitude in meters.
##############################################################################################################################################

def problemB():
    period = int(input("What is the period of the satelite?: "))
    print("The satelites required altitude is: " + str(altitudecalculator(period)) + " km")
    main()

##############################################################################################################################################################
#    c) Use your program to calculate the altitudes of satellites that orbit the Earth once
#       a day (so-called “geosynchronous” orbit), once every 90 minutes, and once every 45 minutes. What do you conclude from the last of these calculations?
##############################################################################################################################################################

def problemC():
    altitudes = [86400, 86148, 5400, 2700]
    for i in altitudes:
        print("The altitude of a satelite with period of" + str(i) + " seconds is " + str(altitudecalculator(i)))
    main()

#####################################################################################################################################
#    d) Technically a geosynchronous satellite is one that orbits the Earth once persidereal
#       day, which is 23.93 hours, not 24 hours. Why is this? And how much difference will it make to the altitude of the satellite?
#####################################################################################################################################

def problemD():
    print("A sidereal day is shorter than 24 hours because of it's orbital motion around the sun. A 24 day refers to the spin of the earth relative to the sun: a Solar day.")
    main()


def main():
    problem = str(input("Please input which problem you'd like to run(a, b, c, d): "))
    if problem == "a":
        problemA()
    elif problem == "b":
        problemB()
    elif problem == "c":
        problemC()
    elif problem == "d":
        problemD()
    else:
        print("You've entered an incorrect choice. Please try again.")

if __name__ == "__main__":
    main()