from manim import *
import numpy as np


class FullCircleSquareExample(Scene):
       
#class halfCircleSquareExample(Scene):
        def construct(self):
            # Define the radius of the circle and the start/end angles for the half circle
            start_angle = 0
            end_angle2 = PI / 2 
            end_angle = PI  # Half of a full circle
            D = Sector(radius=6, start_angle=start_angle, angle=-end_angle, color=GREEN, 
                        fill_opacity=1, stroke_color=[BLUE_A,GREEN_A], stroke_width=2) 
            U = Sector(radius=6, start_angle=start_angle, angle=end_angle, color=GREEN, fill_opacity=1,
                       stroke_color=[BLUE_A,GREEN_A], stroke_width=2)
            BigCircle = Circle(radius=1, color=WHITE, fill_opacity=1, stroke_color=[RED,ORANGE,YELLOW],
                                stroke_width=2, stroke_opacity=0.51)
            
            Qs1 = VGroup(U, D)
            self.play(Write(BigCircle))
            self.play(FadeIn(Qs1), run_time=2)
            self.remove(BigCircle)
            self.play(U.animate.shift(UP * 2), D.animate.shift(DOWN * 2))
    
            
            # Display the filled area and the square
            
            #class QuarterCircleSquareExample(Scene):
        
            # Define the radius of the circle and the start/end angles for the quarter
            
            # Quarter of a full circle

            # Create the filled area representing the quarter circle
            DR = Sector(radius=6, start_angle=start_angle, angle=-end_angle2, color=GREEN, 
                        fill_opacity=1, stroke_color=[BLUE_A,GREEN_A], stroke_width=2) 
            UR = Sector(radius=6, start_angle=start_angle, angle=end_angle2, color=GREEN, fill_opacity=1,
                        stroke_color=[BLUE_A,GREEN_A], stroke_width=2)
            DL = Sector(radius=6, start_angle=-np.pi, angle=end_angle2, color=GREEN, 
                        fill_opacity=1, stroke_color=[BLUE_A,GREEN_A], stroke_width=2)
            UL = Sector(radius=6, start_angle=-np.pi, angle=-end_angle2, color=GREEN, 
                        fill_opacity=1,  stroke_color=[BLUE_A,GREEN_A], stroke_width=2)
            Qs2 = VGroup(DR, UR, DL, UL)
            ############################################################

            self.wait(1)           
            self.play(Write(BigCircle)) 
            self.play(FadeIn(Qs1), run_time=2)
            self.wait(1)
            self.play(FadeIn(Qs2), run_time=2)
            self.wait(1)
            self.remove(BigCircle)
            self.play(DR.animate.shift(DOWN * 1 + RIGHT * 2), UR.animate.shift(UP * 1 + RIGHT * 2),
                       UL.animate.shift(UP * 1 + LEFT * 2), DL.animate.shift(DOWN * 1 + LEFT * 2))
                
            # Display the filled area and the square
            D = Sector(radius=6, start_angle=start_angle, angle=-end_angle, color=GREEN, 
                        fill_opacity=1, stroke_color=[BLUE_A,GREEN_A], stroke_width=2) 
            U = Sector(radius=6, start_angle=start_angle, angle=end_angle, color=GREEN, fill_opacity=1,
                       stroke_color=[BLUE_A,GREEN_A], stroke_width=2)
            BigCircle = Circle(radius=1, color=WHITE, fill_opacity=1, stroke_color=[RED,ORANGE,YELLOW],
                                stroke_width=2, stroke_opacity=0.51)
            
            Qs1 = VGroup(U, D)
            self.play(Write(BigCircle))
            self.play(FadeIn(Qs1), run_time=2)
            self.remove(BigCircle)
            self.play(U.animate.shift(UP * 2), D.animate.shift(DOWN * 2))
    