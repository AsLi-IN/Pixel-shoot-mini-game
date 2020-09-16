import pgzrun
from random import randint
apple=Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x=randint(10,800)
    apple.y=randint(10,600)


def on_mouse_down(pos):
    score=0
    if apple.collidepoint(pos):
        print("GOOD SHOT")
        place_apple()
        score=score+1
    else:
        print("You missed")
        quit()
    
place_apple()
pgzrun.go()
