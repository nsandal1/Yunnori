import turtle
import Tkinter

turtle.home()
turtle.circle(120)

input("Press Enter to continue...")

turtle.left(90)
turtle.begin_poly()

turtle.fd(240)


turtle.fd(-120)

turtle.right(90)

turtle.fd(120)
turtle.fd(-240)
turtle.fd(120)


turtle.end_poly()

p = turtle.get_poly()
register_shape("myFavouriteShape", p)


