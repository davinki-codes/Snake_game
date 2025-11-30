from turtle import Screen
import time
from snake_functioning import Snake
from food import Food
from scoreboard_snake import Scoreboard
from snake_spies import Spies

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor('black')
screen.title('Snake Game')

#2 spies. one will write the title, one will write 'nom-nom'
spy = Spies()
spy.title_spy()
spy_2 = Spies()

screen.tracer(0)

snake = Snake() #calls the createsnake function
food = Food()
scoreboard = Scoreboard()

def restarting_game():
    scoreboard.reset()
    snake.reset()
    spy_2.clear()

screen.listen()
#assign keys for snake control
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.onkey(screen.bye, 'Escape')

game_is_on = True
while game_is_on:
    screen.update()  # updates the animation only after all the segments move
    time.sleep(0.05)  # one-second delay. Placement decides when teh delay takes place

    snake.move() #everytime the screen updates, we need it to move

    #detect collision with food
    if snake.head.distance(food) <= 15:#buffer of 5 pixels
        spy_2.clear()
        print('nom nom nom')
        spy_2.nom_nom((food.xcor(),food.ycor()))
        food.refresh() #changes food position every time there is a collision
        scoreboard.increase_score()
        snake.inc_body_parts()

    #detect collision with boundary
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        restarting_game()


    #detect collision with tail
    for segment in snake.snake_parts[1:]: #cause the first one is the head itself #####################
        if snake.head.distance(segment) <= 5: #the collision must be smaller than one segment
            restarting_game()


screen.exitonclick()