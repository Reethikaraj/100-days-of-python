from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(position)

    def go_up(self):
        if 220 >= self.ycor():
            new_y = self.ycor() + 40
        else:
            new_y = self.ycor()
        self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() >= -220:
            new_y = self.ycor() - 40
        else:
            new_y = self.ycor()
        self.goto(self.xcor(), new_y)
