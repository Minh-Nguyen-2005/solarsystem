#Author: Minh Nguyen
#Date: 10/25/2023
#Purpose: System class

from math import *

class System:
    def __init__(self, body_list):
        #Initialize the system with a list of Body objects as an instance variable.
        self.body_list = body_list

    def draw(self, cx, cy, pixels_per_meter):
        #Method to draw all body objects in the system.
        for body in self.body_list: #call the draw method from Body class for each planet.
            body.draw(cx, cy, pixels_per_meter)

    def update(self, timestep):
        #method calls updates position and velocity of all Body objects in the system.
        # a_x: m/s^2, Acceleration in the x-direction
        # a_y: m/s^2, Acceleration in the y-direction
        for n in range(0, len(self.body_list)):
            self.body_list[n].update_position(timestep)

            (a_x, a_y) = self.compute_acceleration(n)
            self.body_list[n].update_velocity(a_x, a_y, timestep)

    def compute_acceleration(self, n): # Compute the acceleration of each planet (body).
        G = 6.67384e-11 #the universal gravitational constant
        a_x = 0
        a_y = 0

        #position of planet
        xn = self.body_list[n].bx
        yn = self.body_list[n].by

        for i in range(0, len(self.body_list)): #go through all other planets
            check = True
            #positions of each other planets
            xi = self.body_list[i].bx
            yi = self.body_list[i].by
            #mass of each other planets
            mi = self.body_list[i].bmass

            if i == n:
                check = False

            if check:
                dx = xi - xn #x distance
                dy = yi - yn #y distance
                r = sqrt((dx * dx) + (dy * dy)) #total distance between the two bodies
                a = (G * mi) / (r * r)
                ax = a * (dx/r) #x acceleration of planet at index n due to each of the other planets in the list
                ay = a * (dy/r) #y acceleration of planet at index n due to each of the other planets in the list
                a_x = a_x + ax
                a_y = a_y + ay

        return a_x, a_y