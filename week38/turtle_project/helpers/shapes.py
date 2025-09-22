import turtle

def setup_screen(bg_color: str = "lightgrey", title: str = "Turtle Program"):
    screen = turtle.Screen()
    screen.bgcolor(bg_color)
    screen.title(title)
    return screen

def create_turtle(color: str = "black", speed: int = 3, t_shape: str = "turtle") -> turtle.Turtle:
    """
    Lager en turtle
    Kan sette:
    -hastighet
    -farge
    -form
    :return: en turtle.Turtle objekt.
    """
    t = turtle.Turtle()
    t.color(color)
    t.speed(speed)
    t.shape(t_shape)
    return t


def draw_square(t: turtle.Turtle, side_length: int) -> None:
    """
    Tegner en firkant etter ønsket mål
    :param t: et turtle objekt
    :param side_length: hvor lange sider det skal være.
    :return: None
    """

    for _ in range(4):
        t.forward(side_length)
        t.left(90)


def draw_rectangle(t: turtle.Turtle, width: int, height: int) -> None:
    """
    tegner et rektangel
    :param t: turtle objekt
    :param width: lengde på bunn / topp
    :param height: lengde på sider
    :return: None
    """
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def turtle_move_to(t: turtle.Turtle, x: int, y: int) -> None:
    """
    Moves turtle to given coords
    :param x: cordinates
    :param y: cordinates
    :return: None
    """
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_filled_square(t, side_length, fill_color="pink") -> None:
    """
    Draws a filled in square
    :param t: turtle
    :param side_length: sidelenger
    :param fill_color: PINK, don't touch
    :return: None
    """
    t.fillcolor(fill_color)
    t.begin_fill()
    draw_square(t, side_length)
    t.end_fill()
