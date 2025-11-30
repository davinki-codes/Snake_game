from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(-20,250)
        self.hideturtle()
        self.score = 0
        with open('data.txt') as high_score_file:
            self.highscore = int(high_score_file.read())
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode ='w') as high_score_file:
                high_score_file.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER', align = ALIGNMENT, font = FONT)



