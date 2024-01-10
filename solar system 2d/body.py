#Author: Minh Nguyen
#Date: 10/25/2023
#Purpose: Body class

from cs1lib import *

class Body:
    def __init__(self, mass, x, y, v_x, v_y, pixel_radius, r, g, b):
        # Initialize the body object with its provided parameters.
        #Locations
        self.bx = x #m
        self.by = y #m
        #Velocities
        self.vx = v_x #m/s
        self.vy = v_y #m/s

        self.br = r #red color
        self.bg = g #green color
        self.bb = b #blue color
        self.bsize = pixel_radius #radius of body in pixels
        self.bmass = mass #kg

    def draw(self, cx, cy, pixels_per_meter):
        # Method to draw the body.
        #convert the position of the body (stored in meters) into pixel coordinates in the window.
        pixel_x = (self.bx * pixels_per_meter) + cx
        pixel_y = (self.by * pixels_per_meter) + cy

        disable_stroke()
        set_fill_color(self.br, self.bg, self.bb)
        draw_circle(pixel_x, pixel_y, self.bsize)

    def update_position(self, timestep):
        # the x and y locations are updated by the appropriate velocities times the time step.
        self.bx = self.bx + self.vx * timestep
        self.by = self.by + self.vy * timestep

    def update_velocity(self, ax, ay, timestep):
        #the velocities are updated by accelerations ax and ay
        # that will be passed into the method as parameters,
        # as well as the timestep (also passed in as a parameter).
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep