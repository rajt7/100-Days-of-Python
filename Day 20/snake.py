from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEADING = {'up': 90, 'down': 270, 'left': 180, 'right': 0}


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != HEADING['down']:
            self.head.setheading(HEADING['up'])

    def down(self):
        if self.head.heading() != HEADING['up']:
            self.head.setheading(HEADING['down'])

    def left(self):
        if self.head.heading() != HEADING['right']:
            self.head.setheading(HEADING['left'])

    def right(self):
        if self.head.heading() != HEADING['left']:
            self.head.setheading(HEADING['right'])


