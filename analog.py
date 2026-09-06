"""
Analog Clock — turtle graphics
Draws a live analog clock face with hour, minute, and second hands.
"""

import turtle
import time
import math

# ---------- Setup ----------
screen = turtle.Screen()
screen.title("Analog Clock")
screen.bgcolor("black")
screen.tracer(0)  # manual screen updates for smooth animation

RADIUS = 200

# One turtle for the static face (drawn once)
face = turtle.Turtle()
face.hideturtle()
face.speed(0)
face.color("white")
face.pensize(3)

# Separate turtles for each hand
hour_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
second_hand = turtle.Turtle()

for hand in (hour_hand, minute_hand, second_hand):
    hand.hideturtle()
    hand.speed(0)
    hand.pensize(4)

hour_hand.color("white")
minute_hand.color("cyan")
second_hand.color("red")
second_hand.pensize(2)


def draw_face():
    """Draw the circular clock face with hour tick marks and numbers."""
    face.penup()
    face.goto(0, -RADIUS)
    face.pendown()
    face.circle(RADIUS)

    for i in range(60):
        angle = i * 6
        face.penup()
        face.goto(0, 0)
        face.setheading(90 - angle)

        if i % 5 == 0:
            tick_len_outer, tick_len_inner = RADIUS, RADIUS - 15
            face.pensize(3)
        else:
            tick_len_outer, tick_len_inner = RADIUS, RADIUS - 8
            face.pensize(1)

        face.forward(tick_len_inner)
        face.pendown()
        face.forward(tick_len_outer - tick_len_inner)
        face.penup()

    # Numbers 1-12
    face.pensize(1)
    for hour in range(1, 13):
        angle_rad = math.radians(90 - hour * 30)
        x = (RADIUS - 35) * math.cos(angle_rad)
        y = (RADIUS - 35) * math.sin(angle_rad)
        face.goto(x, y - 10)
        face.write(str(hour), align="center", font=("Arial", 16, "bold"))

    # Center dot
    face.goto(0, -6)
    face.dot(12, "white")


def draw_hand(hand, angle_deg, length):
    """Point a hand at the given clock-angle (0 = 12 o'clock, clockwise) with given length."""
    hand.clear()
    hand.penup()
    hand.goto(0, 0)
    hand.setheading(90 - angle_deg)
    hand.pendown()
    hand.forward(length)


def update_clock():
    t = time.localtime()
    hours = t.tm_hour % 12
    minutes = t.tm_min
    seconds = t.tm_sec

    second_angle = seconds * 6
    minute_angle = minutes * 6 + seconds * 0.1
    hour_angle = hours * 30 + minutes * 0.5

    draw_hand(hour_hand, hour_angle, RADIUS * 0.5)
    draw_hand(minute_hand, minute_angle, RADIUS * 0.75)
    draw_hand(second_hand, second_angle, RADIUS * 0.85)

    screen.update()
    screen.ontimer(update_clock, 1000)  # update once per second


draw_face()
screen.update()
update_clock()

screen.mainloop()