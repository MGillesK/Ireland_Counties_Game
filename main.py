import pandas
import turtle

screen = turtle.Screen()
screen.title("Ireland Counties Game")
image = "ireland.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):  +> used to get the coordinate for each county
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)


guessed_counties = []

while len(guessed_counties) < 33:
    answer_county = screen.textinput(title=f"{len(guessed_counties)}/32 Counties Correct",
                                     prompt="What's the state name?").title()

    data = pandas.read_csv("ireland_states.csv")
    list_counties = data.County.to_list()
    list_x = data.x.to_list()
    list_y = data.y.to_list()

    if answer_county == "Exit":
        break

    if answer_county in list_counties:
        guessed_counties.append(answer_county)
        index = list_counties.index(answer_county)
        label = turtle.Turtle()
        label.penup()
        label.goto(list_x[index], list_y[index])
        label.write(answer_county)

counties_to_learn = []
for county in list_counties:
    if county not in guessed_counties:
        counties_to_learn.append(county)


data = pandas.DataFrame(counties_to_learn)
data.to_csv("missed_counties.csv")

screen.exitonclick()
