from manim import *

class ShowWrite(Scene):
    def construct(self):
        T1 = Text("Thank you for your time", font_size=60,gradient=(BLUE , GREEN)).to_edge(UP)
        T2 = MarkupText(f'You could find more about me on my LinkedIn',gradient=(BLUE, GREEN), font_size=40)
        T3= Text("Kamel Senfro",color=YELLOW,font_size=80).to_edge(DOWN)
        #text_group = VGroup(T1, T2)
        ##self.play(Write(Text("Thank you for your time", font_size=144, run_time=3)))

        # Animate writing the text group
        #\n <span fgcolor="{YELLOW}">Kamel Senfro</span>
        
        self.play(Write(T1), run_time=3)
        self.wait(1)
        self.play(Write(T2), run_time=3,reverse=True, remover=False)
        self.wait(1)
        self.play(Write(T3), run_time=2)
        self.wait(3)
        #manim  -pql Name.py ShowWrite