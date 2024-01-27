from tkinter import *
import random

#Game Backbone


BACKGROUND_COLOR = '#0A0A0A'

window = Tk()
window.title('Snake Game')
window.resizable(False, False)

canvas = None


def start():
    global canvas

    canvas = Canvas(window,
                    bg=BACKGROUND_COLOR,
                    width=grid_size[0] * sq_size, height=grid_size[1] * sq_size)
    canvas.pack()

    game_loop()

    window.mainloop()

def update():
    pass

def check_coll():
    pass

def elem():
    canvas.delete("all")
    grid()

is_game_running = True

game_speed = 5 


def game_loop():
    update()
    check_coll()
    elem()

    if is_game_running:
        update_time = int(1000 / game_speed)
        window.after(update_time, game_loop)



#Grid


grid_col = '#222222'

grid_size =(15,15)
sq_size = 40

def grid():
    global canvas

    canvas_width = grid_size[0] * sq_size
    canvas_height = grid_size[1] * sq_size

    for ix in range(grid_size[0]):
        xpos = ix * sq_size
        canvas.create_line(xpos, 0, xpos, canvas_height, width=1, fill=grid_col)

    for iy in range(grid_size[1]):
        ypos = iy * sq_size
        canvas.create_line(0, ypos, canvas_width, ypos, width=1, fill=grid_col)

    

#Snake

snake_col = "green"
snake_cord = [(0,0),(0,0),(0,0)]
curr_dir = "down"
next_dir = "down"

def snake_step():
    global snake_cord, curr_dir

    head = snake_cord[0]
    snake_cord=snake_cord[:-1]

    newhead = None
    if next_dir == "down":
        newhead = (head[0],head[1]+1)
    elif next_dir == "up":
        newhead = (head[0], head[1]-1)
    elif next_dir == "left":
        newhead = (head[0]-1, head[1])
    elif next_dir == "right":
        newhead = (head[0]+1, head[1])

    snake_cord.insert(0, newhead)
    curr_dir=next_dir


def drsnake():
    global canvas
    for x, y in snake_cord:
        x1 = x * sq_size
        y1 = y * sq_size

        x2 = (x+1) * sq_size
        y2 = (y+1) * sq_size

        canvas.create_rectangle(x1,y1,x2,y2, fill = snake_col)


def snake_coll():
    pass

#Food

#Score


if __name__ == '__main__':
    start()