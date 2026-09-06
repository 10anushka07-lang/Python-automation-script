"""
Heart + Synced Lyrics — turtle graphics
Draws the heart while lyric lines type onto the canvas in sync with a song
you play separately (e.g. on your phone), using ABSOLUTE timestamps from
song-start (not stacked delays, which drift). You hit Enter the moment you
press play, and that becomes timestamp 0.0 for everything in TIMESTAMPS.

NOTE: Replace the placeholder strings in LYRICS with your own lyric lines,
and fill in TIMESTAMPS below.
"""

import turtle
import math
import random
import time

# ---------- Lyrics (replace with your own lines, in order) ----------
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
        "You got me turnin' all around to be who you need me to \n "]  # 33 placeholders

# ---------- Sync timing ----------
# ABSOLUTE seconds from the moment the song starts playing — not "wait this
# long after the last line." This is what keeps things in sync with real
# audio, because each line is checked against actual elapsed time instead
# of accumulating drift from previous sleeps.
#
# Fill this in by listening to the track (or pulling timestamps from an
# .lrc file if you have one) and noting the second each line begins.
# Must be the same length as LYRICS, and strictly increasing.
TIMESTAMPS = [round(n * 5.0, 1) for n in range(len(LYRICS))]  # <-- placeholder spacing, replace with real times

if len(TIMESTAMPS) != len(LYRICS):
    raise ValueError(f"{len(TIMESTAMPS)} timestamps but {len(LYRICS)} lyric lines — these must match exactly.")

SONG_TITLE = "your song title here"

# ---------- Turtle setup ----------
screen = turtle.Screen()
screen.title("Happy Birthday!")
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

writer = turtle.Turtle()
writer.hideturtle()
writer.speed(0)
writer.color("white")
writer.penup()
writer.goto(0, -260)

CURRENT_LINE = ""  # what's fully shown right now, so we don't retype from scratch every frame


def show_line_instant(line):
    """Show a full line immediately (used once its timestamp is reached)."""
    global CURRENT_LINE
    CURRENT_LINE = line
    writer.clear()
    writer.goto(0, -260)
    writer.write(line, align="center", font=("Arial", 16, "normal"))


colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"]

TOTAL_POINTS = 120
HEART_STEP_DELAY = 0.03  # small pause between heart segments

title_writer = turtle.Turtle()
title_writer.hideturtle()
title_writer.speed(0)
title_writer.color("gray")
title_writer.penup()
title_writer.goto(0, 220)
title_writer.write(SONG_TITLE, align="center", font=("Arial", 14, "italic"))
screen.update()

# ---------- Manual sync point ----------
# Hit Enter here at the exact moment you press play on your phone.
# That instant becomes timestamp 0.0 for everything in TIMESTAMPS.
input("Press Enter the moment you hit play on the song...")
song_start = time.time()

lyric_index = 0
heart_index = 0

# Run until both the heart is done AND all lyrics have been shown
while heart_index < TOTAL_POINTS or lyric_index < len(LYRICS):

    # Draw the next heart segment, if any left
    if heart_index < TOTAL_POINTS:
        t.penup()
        t.goto(0, 40)

        angle = heart_index * (math.pi * 2) / TOTAL_POINTS
        x = 16 * (math.sin(angle) ** 3) * 15
        y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 15

        t.color(random.choice(colors))
        t.pendown()
        t.goto(x, y)

        for _ in range(8):
            t.forward(6)
            t.backward(6)
            t.right(45)

        heart_index += 1

    # Check real elapsed time against the song clock, not a sleep counter —
    # this is what keeps lyrics locked to the audio even if a frame runs slow.
    elapsed = time.time() - song_start
    if lyric_index < len(LYRICS) and elapsed >= TIMESTAMPS[lyric_index]:
        show_line_instant(LYRICS[lyric_index])
        lyric_index += 1

    screen.update()
    time.sleep(HEART_STEP_DELAY)

turtle.done()