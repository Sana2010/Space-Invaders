from scoreboard import Scoreboard
from projectile import Shuriken
from player import Shredder
from turtle import Screen
from levels import Level
import random
import time

GAME_ON = True
LEVEL = 1

scoreboard = Scoreboard()
player = Shredder(0, -300)
level = Level()

screen = Screen()
screen.setup(width=700, height=650)
screen.bgcolor("black")
screen.title("TurtleInvaders")
screen.tracer(0)

screen.listen()
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")
screen.onkey(player.throw_katana, 'space')

shuriken_list = []
level.load_ninjas(LEVEL)
count = 0
move_count = 0
direction = 'left'
while GAME_ON:
    screen.update()
    count += 1
    move_count += 1
    time.sleep(0.01)
    level.move_ninjas(direction)
    if move_count == 200:
        direction = level.switch_dir(direction)
        move_count = 0

    if not level.ninja_list:
        for shuriken in shuriken_list:
            shuriken.reset()
        for katana in player.katana_list:
            katana.reset()
        shuriken_list = []
        player.clear_katanas()
        LEVEL += 1
        if LEVEL > 3:
            scoreboard.you_win()
            time.sleep(2)
            GAME_ON = False
        move_count = 0
        direction = 'left'
        scoreboard.new_level()
        scoreboard.update_level()
        level.load_ninjas(LEVEL)

    if count == 25:
        random_ninja = level.ninja_list[random.randint(0, len(level.ninja_list) - 1)]
        new_shuriken = Shuriken(random_ninja)
        shuriken_list.append(new_shuriken)
        count = 0
    # Detect Shuriken(enemy projectile) Collision with Player object
    for shuriken in shuriken_list:
        if shuriken.ycor() < -300:
            shuriken_list.remove(shuriken)
        shuriken.move_shuriken()
        player.move_katanas()
        if shuriken.distance(player) < 20 and shuriken.ycor() < -290:
            scoreboard.you_lose()
            GAME_ON= False
        elif shuriken.ycor() < -300:
            shuriken.reset()
            shuriken_list.remove(shuriken)
    # Detect Katana(player projectile) Collision with Ninja objects
    for ninja in level.ninja_list:
        for katana in player.katana_list:
            if ninja.distance(katana) < 15:
                ninja.reset()
                level.ninja_list.remove(ninja)
                player.delete_katana(katana)

screen.exitonclick()