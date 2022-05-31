import pandas
import turtle
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



s = pandas.read_csv("50_states.csv")
s_list = list(s.state)
guess = True
score = 0

while guess:
  
  answer_state = str(screen.textinput(f"{score}/50 States Correct", "What's another State name?").capitalize())
  
  if answer_state in s_list:
    cor = s[s["state"] == f'{answer_state}']
    x_cor = int(cor.x)
    y_cor = int(cor.y)
    cord = list((x_cor, y_cor))
    #cord_list.append(cord)
    print(cord)
    s_list.remove(f'{answer_state}')
    t = turtle.Turtle()
    t.shape('square')
    t.penup()
    t.hideturtle()
    t.goto(cord)
    t.write(f'{answer_state}',align = 'center', font = ('Arial', 10, 'italic'))
    score += 1
    
  elif score == 50:
    guess = False

  else:
    pass

screen.exitonclick()

