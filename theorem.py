from manim import *
import numpy as np

# Configured to be a vertical video
config.pixel_height = 1920
config.pixel_width = 1080
config.background_color = BLACK


class pyProof(MovingCameraScene):
    def construct(self):

        def place_next_to_edge(shape, edge_number, distance=0.5):
            def updater(mob, dt):
                vertices = shape.get_vertices()
                edge = vertices[edge_number-1] - vertices[edge_number]
                edge_center = vertices[edge_number] + edge/2
                edge /= np.linalg.norm(edge)
                edge_normal = np.array([edge[1], -edge[0], 0])
                mob.move_to(edge_center).shift(distance*edge_normal)
            return updater

        grid = NumberPlane(color=YELLOW)

        # Create triangles
        triangleOne = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                              color=TEAL_C, fill_opacity=0.5)

        triangleTwo = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                              color=TEAL_C, fill_opacity=0.5)

        triangleThree = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                color=TEAL_C, fill_opacity=0.5)

        triangleFour = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                               color= TEAL_C  , fill_opacity=0.5)

        # Create angle lines
        angleLineOne = Line([-4, -3, 0], [-4, -2, 0], color = [PURE_GREEN,TEAL_C])
        angleLineTwo = Line([-4, -2, 0], [-5, -2, 0], color=[PURE_GREEN,TEAL_C])

        # Create big square
        bigSquare = Polygon([-5, -3, 0], [-5, 7, 0],
                            [5, 7, 0], [5, -3, 0], fill_color=PURPLE_A, fill_opacity=0.75, stroke_color=PURPLE_B)
        bigSquareArea = Polygon([-5, -3, 0], [-5, 7, 0],
                                [5, 7, 0], [5, -3, 0], fill_color=PURPLE_A, fill_opacity=0.75, stroke_color=PURPLE_D)

        # Create small square
        smallSquareColor = Polygon([-5, 1, 0], [-1, 7, 0],
                                   [5, 3, 0], [1, -3, 0], fill_color=BLUE_C, fill_opacity=0.5)
        smallSquare = Polygon([-5, 1, 0], [-1, 7, 0],
                              [5, 3, 0], [1, -3, 0], fill_color=BLUE_C, fill_opacity=0.5)

        # Create labels for triangles
        # aOne = Tex("a").color(YELLOW)
        # aTwo = Tex("a").color(YELLOW)
        # aThree = Tex("a").color(YELLOW)
        # aFour = Tex("a").color(YELLOW)
        # bOne = Tex("b").color(YELLOW)
        # bTwo = Tex("b").color(YELLOW)
        # bThree = Tex("b").color(YELLOW)
        # bFour = Tex("b").color(YELLOW)
        # cOne = Tex("c").color(YELLOW)
        # cTwo = Tex("c").color(YELLOW)
        # cThree = Tex("c").color(YELLOW)
        # cFour = Tex("c").color(YELLOW)
        aOne = Text("a", color=YELLOW, font="Minion Pro SmBd")
        bOne = Text("b",color=YELLOW, font="Minion Pro SmBd")
        cOne = Text("c", color=YELLOW, font="Minion Pro SmBd")
        aTwo = Text("a", color=YELLOW, font="Minion Pro SmBd")
        bTwo = Text("b", color=YELLOW, font="Minion Pro SmBd")
        cTwo = Text("c", color=YELLOW, font="Minion Pro SmBd")
        aThree = Text("a", color=YELLOW, font="Minion Pro SmBd")
        bThree = Text("b", color=YELLOW, font="Minion Pro SmBd")
        cThree = Text("c", color=YELLOW, font="Minion Pro SmBd")
        aFour = Text("a", color=YELLOW, font="Minion Pro SmBd")
        bFour = Text("b", color=YELLOW, font="Minion Pro SmBd")
        cFour = Text("c", color=YELLOW, font="Minion Pro SmBd")

        labelsOne = VGroup(aOne, bOne, cOne)
        labelsTwo = VGroup(aTwo, bTwo, cTwo)
        labelsThree = VGroup(aThree, bThree, cThree)
        labelsFour = VGroup(aFour, bFour, cFour)

        for i, label in enumerate(labelsOne):
            label.add_updater(place_next_to_edge(
                triangleOne, i), call_updater=True)

        for i, label in enumerate(labelsTwo):
            label.add_updater(place_next_to_edge(
                triangleTwo, i), call_updater=True)

        for i, label in enumerate(labelsThree):
            label.add_updater(place_next_to_edge(
                triangleThree, i), call_updater=True)

        for i, label in enumerate(labelsFour):
            label.add_updater(place_next_to_edge(
                triangleFour, i), call_updater=True)

        # self.add(grid)
        self.add(self.camera.frame)
        self.camera.frame.save_state()

        # Animation sequence
        self.play(
            AnimationGroup(
                self.camera.frame.animate.move_to(triangleOne),
                Write(triangleOne),
                lag_ratio=0.5
            )
        )

        self.play(
            AnimationGroup(
                FadeIn(angleLineOne),
                FadeIn(angleLineTwo),

                lag_ratio=0.2
            ), run_time=0.8
        )

        self.wait(0.25)

        self.play(
            AnimationGroup(
                FadeOut(angleLineOne),
                FadeOut(angleLineTwo),
                lag_ratio=0.2
            ), run_time=0.8
        )

        self.play(Write(labelsOne))

        self.play(Write(triangleTwo), run_time=0.5)

        self.play(
            triangleTwo.animate.shift(5*RIGHT+UP),
            Write(labelsTwo),
            self.camera.frame.animate.restore(),
            lag_ratio=0.5
        )

        self.play(Rotate(triangleTwo, PI/2))

        self.play(Write(triangleThree), Write(triangleFour), run_time=0.5)

        self.play(
            AnimationGroup(
                self.camera.frame.animate.shift(3*UP),
                AnimationGroup(
                    triangleThree.animate.shift(4*RIGHT+6*UP),
                    Write(labelsThree),
                    lag_ratio=0.2,
                ),
                AnimationGroup(
                    triangleFour.animate.shift(5*UP+LEFT),
                    Write(labelsFour),
                    lag_ratio=0.2,
                ),
                lag_ratio=0.4,
                run_time=1.6
            )
        )

        self.play(
            AnimationGroup(
                Rotate(triangleThree, -PI),
                Rotate(triangleFour, -PI/2),
                lag_ratio=0.4
            )
        )

        self.wait(1)

        self.play(Write(bigSquare))

        self.play(FadeOut(bigSquare))

        self.play(self.camera.frame.animate.shift(5*DOWN))

        # DECLARATIONS FOR PART WITH EQUATIONS

        areaLabel = MathTex("A_{BigSquare}").shift(6*DOWN + 5.5*LEFT)
        eqEqual = MathTex("=").next_to(areaLabel, RIGHT)

        smallTriangleOne = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                   color=TEAL_C, fill_opacity=0.7)
        smallTriangleTwo = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                   color=TEAL_C, fill_opacity=0.7).shift(5*RIGHT+UP).rotate(PI/2)
        smallTriangleThre = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                    color=TEAL_C, fill_opacity=0.7).shift(4*RIGHT+6*UP).rotate(-PI)
        smallTriangleFour = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                    color=TEAL_C, fill_opacity=0.7).shift(5*UP+LEFT).rotate(-PI/2)
        plusOne = Text("+", color   = YELLOW_C).shift(6*DOWN-1.5*RIGHT)
        plusTwo = Text("+", color   = YELLOW_C).shift(6*DOWN+0.5*RIGHT)
        plusThree = Text("+", color = YELLOW_C).shift(6*DOWN+2.5*RIGHT)
        plusFour = Text("+",color   = YELLOW_C).shift(6*DOWN+4.5*RIGHT)
 
        finalSmallTriangle = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                     color=TEAL_B, fill_opacity=0.8).move_to([-1.5, -6, 0]).scale(0.2)
        fourTimes = MathTex(r"4 \times").move_to([-2.5, -6, 0])
        triangleEquationOne = VGroup(smallTriangleOne, smallTriangleTwo,
                                     smallTriangleThre, smallTriangleFour, plusOne, plusTwo, plusThree)
        triangleEquationTwo = VGroup(
            fourTimes, finalSmallTriangle).move_to([0.5, -7, 0])
        squareEquation = VGroup(plusFour, smallSquare)

        # ANIMATIONS EQUATIONS

        # Write big square area and big square
        self.play(Write(bigSquareArea), Write(bigSquare), run_time=0.5)

        # Move big square area and write equal sign
        self.play(bigSquareArea.animate.move_to(
            [-5.5, -6, 0]).scale(0.1), Write(eqEqual), FadeOut(bigSquare))

        # Fade in green color for all triangles
        self.play(
            FadeToColor(triangleOne, color=TEAL_C),
            FadeToColor(triangleTwo, color=TEAL_C),
            
            FadeToColor(triangleThree,color= TEAL_C),
            FadeToColor(triangleFour,color= TEAL_C),
            run_time=0.5
        )

        # Move and scale small triangles, fade in plus signs
        self.play(
            AnimationGroup(
            AnimationGroup(
                smallTriangleOne.animate.move_to([-2.5, -6, 0]).scale(0.2),
                smallTriangleTwo.animate.move_to([-0.5, -6, 0]).scale(0.2),
                smallTriangleThre.animate.move_to([1.5, -6, 0]).scale(0.2),
                smallTriangleFour.animate.move_to([3.5, -6, 0]).scale(0.2),
            ),
            AnimationGroup(
                FadeIn(plusOne),
                FadeIn(plusTwo),
                FadeIn(plusThree)
            ),
            lag_ratio=0.5
            )
        )

        # Fade in small square color
        self.play(FadeIn(smallSquareColor), run_time=0.5)

        # Move and scale small square, fade in plus sign
        self.play(
            AnimationGroup(
            smallSquare.animate.move_to(
                [5.5, -6, 0]).scale(0.125),
            FadeIn(plusFour),
            lag_ratio=0.5
            )
        )

        # Move and transform triangle equation to square equation, shift square equation and big square area
        self.play(ReplacementTransform(triangleEquationOne, triangleEquationTwo),
              squareEquation.animate.shift(2.5*LEFT+DOWN), VGroup(bigSquareArea, eqEqual).animate.shift(3*RIGHT+DOWN))

        self.wait(2)

        # Add underbraces and write equations
        underbraceOne = MathTex(r"\underbrace{}").move_to([0.5, -8, 0])
        underbraceTwo = MathTex(r"\underbrace{}").move_to([3, -8, 0])
        underbraceThree = MathTex(r"\underbrace{}").move_to([-2.5, -8, 0])

        triangleEq = MathTex(r"4 \times \frac{ab}{2}").move_to(
            [0.5, -9, 0])
        newTriangleEq = MathTex(r"2ab").move_to(
            triangleEq.get_center())
        smallSquareEq = MathTex(r"c^2").move_to([3, -9, 0])

        bSquareEq = MathTex("(a+b)^2").move_to([-2.5, -9, 0])
        newBSquareEq = MathTex(
            "a^2+2ab+b^2").move_to(bSquareEq.get_center())

        plusFive = Tex("+").move_to([2, -9, 0])
        eqEqualTwo = MathTex("=").move_to([-0.5, -9, 0])

        self.play(Write(underbraceOne), run_time=0.5)
        self.play(Write(triangleEq))
        self.play(Write(underbraceTwo), run_time=0.5)
        self.play(Write(smallSquareEq), Write(plusFive))

        self.play(ReplacementTransform(triangleEq, newTriangleEq),
              plusFive.animate.shift(LEFT*0.5), smallSquareEq.animate.shift(LEFT*0.75), FadeOut(underbraceOne), FadeOut(underbraceTwo))

        self.wait(1)

        self.play(Write(underbraceThree), run_time=0.5)
        self.play(Write(bSquareEq), Write(eqEqualTwo))

        self.play(ReplacementTransform(bSquareEq, newBSquareEq),
              eqEqualTwo.animate.shift(RIGHT*0.5), FadeOut(underbraceThree), VGroup(plusFive, smallSquareEq, newTriangleEq).animate.shift(RIGHT))

        self.wait(1)

        finalEq = MathTex("a^2+b^2 = c^2", color= YELLOW).move_to(VGroup(newBSquareEq, eqEqualTwo,
                                  newTriangleEq, smallSquareEq, plusFive).get_center())

        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(newBSquareEq, smallSquareEq,
              newTriangleEq), finalEq), FadeOut(eqEqualTwo), FadeOut(plusFive))

        self.wait(2)

        # Fade out unnecessary elements and move triangle one and final equation
        self.play(
            FadeOut(
            bigSquareArea,
            triangleEquationTwo, squareEquation, eqEqual,
            triangleTwo, triangleThree, triangleFour, smallSquareColor,
            aTwo, bTwo, cTwo, aThree, bThree, cThree, aFour, bFour, cFour
            ),
            triangleOne.animate.move_to([0, -1, 0]).scale(2),
            finalEq.animate.move_to([0, -7.5, 0]).scale(2)
        )

        self.wait(3)
