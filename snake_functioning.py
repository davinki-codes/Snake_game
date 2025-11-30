from turtle import Turtle

COORDINATES = [(0, 0), (-10, 0), (-20, 0)]
move_distance = 10 #keep constant so you can change whenever
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.createsnake()
        self.move()
        self.head = self.snake_parts[0]

    def add_segment(self,position):
        p = Turtle(shape='square')
        p.color('white')  # adds fill color and pen color
        p.shapesize(stretch_wid=0.5, stretch_len=0.5)
        p.penup()
        p.goto(position)
        self.snake_parts.append(p)   #creates a white block, and adds it wherever you tell it to


    def inc_body_parts(self):
        last = self.snake_parts[-1]
        new_pos = (last.xcor(),last.ycor()) #dont skip the brackets
        self.add_segment(new_pos)    #you're telling it to add segment at the end

    def createsnake(self):
        starting_coordinates = COORDINATES
        for position in starting_coordinates:  # create snake body with 3 squares - 20px lined after each other
            self.add_segment(position)

    def reset(self): #restart the snake
        for seg in self.snake_parts:
            seg.goto(1000,1000) #to remove the dead snake from the screen
        self.snake_parts.clear()
        self.createsnake()
        self.head = self.snake_parts[0]

    def move(self):
        for i in range(len(self.snake_parts)-1,0,-1): #(start, stop, step) - take steps back ##########
            new_x = self.snake_parts[i-1].xcor()
            new_y = self.snake_parts[i-1].ycor()
            self.snake_parts[i].goto(x=new_x,y=new_y)
        self.snake_parts[0].forward(move_distance)
        # head = self.snake_parts[0]

    def up(self):
        if self.snake_parts[0].heading() != DOWN: #270 better than -90
            self.snake_parts[0].setheading(UP)

    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)

    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)

    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)

