"""
Snake Game — turtle graphics
Arrow keys to move. Eat the food, don't hit yourself or the walls.
"""

import turtle
import time
import random

# ---------- Setup ----------
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # manual updates for smooth, controllable speed

WIDTH, HEIGHT = 600, 600
STEP = 20
delay = 0.1

score = 0
high_score = 0

# ---------- Snake head ----------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

segments = []

# ---------- Food ----------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# ---------- Score display ----------
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, HEIGHT / 2 - 40)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + STEP)
    if head.direction == "down":
        head.sety(head.ycor() - STEP)
    if head.direction == "left":
        head.setx(head.xcor() - STEP)
    if head.direction == "right":
        head.setx(head.xcor() + STEP)


# ---------- Keyboard bindings ----------
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")


def reset_game():
    global score, delay, segments
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.hideturtle()
    segments.clear()

    score = 0
    delay = 0.1
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))


# ---------- Main game loop ----------
while True:
    screen.update()

    # Wall collision
    if (head.xcor() > WIDTH / 2 - 10 or head.xcor() < -WIDTH / 2 + 10 or
            head.ycor() > HEIGHT / 2 - 10 or head.ycor() < -HEIGHT / 2 + 10):
        reset_game()

    # Food collision
    if head.distance(food) < 15:
        x = random.randint(-int(WIDTH / 2 - 20), int(WIDTH / 2 - 20))
        y = random.randint(-int(HEIGHT / 2 - 20), int(HEIGHT / 2 - 20))
        # snap to grid so it lines up with the snake's steps
        x = round(x / STEP) * STEP
        y = round(y / STEP) * STEP
        food.goto(x, y)

        # Add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        delay = max(0.05, delay - 0.001)  # speed up slightly

        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

    # Move segments in reverse order (each takes the position of the one in front)
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision
    for segment in segments:
        if segment.distance(head) < 10:
            reset_game()

    time.sleep(delay)