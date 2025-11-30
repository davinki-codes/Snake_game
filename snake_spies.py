from turtle import Turtle

class Spies(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()

    def title_spy(self):
        position = (-20,-265)
        self.goto(position)
        self.write(f'HUNGWY HUNGWY SNAKE', align='center', font=('Courier', 25, 'normal'))

    def nom_nom(self,position):
        self.goto(position)
        self.color('green')
        self.write(f'nom nom', align='center', font=('Courier', 10, 'normal'))

    def you_lost(self):
        self.clear()
        position = (-20,-265)
        self.goto(position)
        self.write(f'YOU LOST YA IDIOTE :D', align='center', font=('Courier', 25, 'normal'))
