import helpers as h
import turtle


def main():
    s = h.setup_screen("lightgrey", "Turtle Square")
    t = h.create_turtle("black", 2, "turtle")
    h.draw_square(t, 150)

    h.turtle_move_to(t, -300, 150)
    h.draw_rectangle(t, 250, 200)

    h.turtle_move_to(t, 0, -250)

    h.draw_filled_square(t, 200, "pink")

    s.mainloop()

if __name__ == "__main__":
    main()