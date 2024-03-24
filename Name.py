from manim import *

class QuarterCircleSquareExample(Scene):
    def construct(self):
        # Define the radius of the circle and the start/end angles for the quarter
        radius = 1
        start_angle = 0
        end_angle = PI / 2  # Quarter of a full circle

        # Create the filled area representing the quarter circle
        quarter_fill = Sector(radius=radius, start_angle=start_angle, angle=-end_angle, color=GREEN, fill_opacity=0.5)  # Adjust opacity as needed

        # Create a square behind the circle
        square = Circle(radius=2*radius, color=WHITE, fill_opacity=0.5)

        # Display the filled area and the square
        self.play(Create(quarter_fill)) 
        self.wait(1)
        self.play(Create(square))
       
