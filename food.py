from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #default is 20 pixels, we are make it 10 smaller
                                                        # now each dot is 10 pixels
        self.color('green')
        self.speed('fastest')
        self.refresh() #inside a class, you can refer to its own functions


    def refresh(self):
        random_x = random.randint(-270,270) #because our screen is 600 wide
        random_y = random.randint(-240,270)
        self.goto(x=random_x,y=random_y)


