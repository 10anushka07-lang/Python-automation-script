"""
Heart + Synced Lyrics — turtle graphics
Draws the heart one segment at a time. Each time it finishes a segment,
the next lyric line types out in the console like a typewriter.

NOTE: Replace the placeholder strings in LYRICS with your own lyric lines.
(Left as placeholders here — not filling in actual song lyrics.)
"""

import turtle
import math
import random
import time
import sys

# ---------- Lyrics (replace these with your own 33 lines, in order) ----------
LYRICS = ["Maybe I shouldn't try to be perfect\n",
        "I confess that I am obssesed with the surface\n",
        "In the end, if I fall or if I get it all\n",
        "I just hope that it's worth it\n",
        "Last year I fell flat on my face\n",
        "And last month I knew somethin' should change\n",
        "Last week I started over again\n",
        "Ask me and I'll tell you how I've been\n",
        "Mm, don't get me started\n",
        "You've got me nervous to speak\n",
        "So I just won't say anything at all\n",
        "I've got an urge to release\n",
        "And you keep tellin' me to hold on\n",
        "You've got me nervous to move\n",
        "So I just won't give anything to you\n",
        "You got me turnin' all around to be who you need me to\n",
        "Should I be quiet? Uh \n",
        "Come on, be silent, uh \n",
        "You know I'm tryin', so don't say nothin', uh\n",
        "Tell me you trust me, and \n",
        "Kiss me and hug me, yeah \n",
        "Well, I would do anything for ya \n",
        "You just gotta love me, and- \n",
        "I got an itch in my throat\n ",
        "I don't know which way to go \n", 
        "I keep on switchin', I know \n",
        "I need a different approach \n",
        "It's all because I wanna show you that I'm so capable \n",
        "You've got me nervous to speak \n",
        "So I just won't say anything at all \n",
        "I've got an urge to release\n              ",
        "And you keep tellin' me to hold on \n                       ",
        "You've got me nervous to move\n",
        "So I just won't give anything to you \n",
        "You got me turnin' all around to be who you need me to \n "]  

SONG_TITLE = "nervous by neighborhood"
DELAYS = [[300] + [350] * 20+ [350] * (len(LYRICS) - 21



                                       )]  # Delay in milliseconds for each lyric line
# ---------- Turtle setup ----------
screen = turtle.Screen()
screen.title("")
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

# Separate turtle just for writing lyrics on screen, below the heart
writer = turtle.Turtle()
writer.hideturtle()
writer.speed(0)
writer.color("white")
writer.penup()
writer.goto(0, -260)


def type_line_on_screen(line, char_delay=0.095):
    """Type a line onto the canvas character by character, replacing the last line."""
    partial = ""
    for char in line:
        writer.clear()
        partial += char
        writer.goto(0, -260)
        writer.write(partial, align="center", font=("Arial", 16, "normal"))
        screen.update()
        time.sleep(char_delay)


colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"]

TOTAL_POINTS = 120

# Work out which heart-segment indices should trigger the next lyric line,
# spread evenly across the full drawing.
if LYRICS:
    trigger_every = TOTAL_POINTS / len(LYRICS)
    trigger_points = {int(i * trigger_every) for i in range(len(LYRICS))}
else:
    trigger_points = set()

title_writer = turtle.Turtle()
title_writer.hideturtle()
title_writer.speed(0)
title_writer.color("gray")
title_writer.penup()
title_writer.goto(0, 220)
title_writer.write(SONG_TITLE, align="center", font=("Arial", 14, "italic"))
screen.update()
time.sleep(1.0)

lyric_index = 0

for i in range(TOTAL_POINTS):
    t.penup()
    t.goto(0, 40)

    angle = i * (math.pi * 2) / TOTAL_POINTS

    x = 16 * (math.sin(angle) ** 3) * 15
    y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 15

    c = random.choice(colors)
    t.color(c)

    t.pendown()
    t.goto(x, y)

    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

    screen.update()

    # Type the next lyric line on screen when we hit a trigger point
    if i in trigger_points and lyric_index < len(LYRICS):
        type_line_on_screen(LYRICS[lyric_index])
        lyric_index += 1
    else:
        time.sleep(0.04)  # small pause so the heart still unfolds visibly

# In case any lyric lines are left over, type them after the heart finishes
while lyric_index < len(LYRICS):
    type_line_on_screen(LYRICS[lyric_index])
    lyric_index += 1

turtle.done()