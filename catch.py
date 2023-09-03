import turtle
import random

screen1 = turtle.Screen()
screen1.bgcolor("light blue")
screen1.title("Catch Turtle")
FONT = ("Arial", 30, "normal")
turtle_lists = []
score = 0
score_turtle = turtle.Turtle()

countdown_turtle = turtle.Turtle()

game_over = False


# score turtle


def setup_turtle_score():
    score_turtle.hideturtle()

    score_turtle.color("dark blue")

    score_turtle.penup()
    screen_height = turtle.window_height() / 2
    y = screen_height * 0.8

    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score:0", move=False, align="center", font=FONT)


grid_size = 10


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.color("dark green")
    t.shapesize(2, 2)
    t.goto(x * grid_size, y * grid_size)
    turtle_lists.append(t)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-10, 0, 10, 20]


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():
    for t in turtle_lists:
        t.hideturtle()


def show_turtle_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_lists).showturtle()
        screen1.ontimer(show_turtle_randomly, 1000)


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")

    countdown_turtle.penup()
    screen_height = turtle.window_height() / 2
    y = screen_height * 0.8

    countdown_turtle.setposition(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen1.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)


def start_game_up():
    turtle.tracer(0)

    setup_turtle_score()
    setup_turtles()

    hide_turtles()
    show_turtle_randomly()
    countdown(10)

    turtle.tracer(1)


start_game_up()
screen1.mainloop()




