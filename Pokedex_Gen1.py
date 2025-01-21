import turtle as t

print("welcome to the pokedex")
user_input = (str(input("Please type charizard: ")))

if user_input == "charizard":
    Screen = t.Screen()
    Screen.title = ("pokedex")
    t = t.Turtle()
    t.fillcolor('red')
    t.penup() #turtle doesnt draw while moving
    t.goto(-150,250) #horizontal,vertical
    t.pendown() #place down pen
    t.begin_fill()
    width = 300
    length = 200
    for _ in range (2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)

    t.end_fill()

    t.fillcolor("red")
    t.penup()
    t.goto(-150,-385)
    t.pendown()
    t.begin_fill()
    width = 300
    length = 200
    for _ in range (2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(0,295)
    t.color("white")
    t.write("POKEDEX", align="center", font = ("Courier",24,"bold"))

    t.penup()
    t.goto(-151, 392)
    t.pendown()
    t.color("black")
    t.setheading(270)
    t.forward(800)

    t.penup()
    t.goto(151, 392)
    t.pendown()
    t.color("black")
    t.setheading(270)
    t.forward(800)

    t.penup()
    t.goto(-151, -281)
    t.pendown()
    t.color("black")
    t.setheading(0)
    t.forward(300)

    t.penup()
    t.goto(21,-280)
    t.setheading(90)
    t.pendown()
    t.color("black")
    t.circle(20,180)

    t.fillcolor("white")
    t.pen()
    t.goto(-19,-280)
    t.setheading(270)
    t.pendown()
    t.begin_fill()
    t.circle(20,180)
    t.end_fill()


    t.fillcolor("white")
    t.penup()
    t.goto(4, -280)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    Screen.bgpic("C:/Users/adsol/Downloads/merged (1).gif")
    Screen.register_shape("C:/Users/adsol/Downloads/merged (1).gif")
    t.shape("C:/Users/adsol/Downloads/merged (1).gif")
    t.shapesize(stretch_wid=.5,stretch_len=.5)
    t.penup()
    t.goto(0,0) #can easily be turned into an if statement ex: if user enters pokemon name execute this with a photo of them

    def display_coords(x,y):
        t.clear()
        t.goto(x,y)
        t.write(f"({x:.0f}, {y:.0f})", align = "left", font = ("Arial",12,"normal"))
    Screen.onscreenclick(display_coords)

    t.hideturtle()

    Screen.mainloop()
