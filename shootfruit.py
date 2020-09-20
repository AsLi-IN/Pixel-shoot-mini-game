import pgzrun
import pygame
from random import randint
apple=Actor("apple")
game_over=False
score=0
def draw():
    screen.clear()
    screen.fill("light green")
    screen.draw.text("Score "+str(score),color=("violet"),topleft=(10,10),fontsize=60)
    apple.draw()
    if game_over:
        screen.fill("black")
        screen.draw.text(" GAME OVER ",color=("DARK RED"),topleft=(250,10),fontsize=60)
        screen.draw.text("YOUR FINAL SCORE WAS : "+str(score),color=("white"),topleft=(210,90),fontsize=40)

def place_apple():
    apple.x=randint(10,800)
    apple.y=randint(10,600)


def on_mouse_down(pos):
    global score
    global game_over
    if apple.collidepoint(pos):
        place_apple()
        score=score+1
    else:
        game_over=True
        print("You missed")
    
place_apple()
pgzrun.go()
