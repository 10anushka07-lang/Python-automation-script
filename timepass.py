import sys
import time  

def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()  

def print_lyrics():
    lyrics = [
       
        "Maybe I shouldn't try to be perfect\n",
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
        "You got me turnin' all around to be who you need me to \n "
        
    ]
    delays = [1.8,1.8,1.8,2.0,1.8,1.,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6]  # Adjust delays for each line

    print("nervous by the neighborhood:\n")
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])


print_lyrics()
time.sleep(0.02)