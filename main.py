import turtle
from math import comb


def pascal(rowNum): # generates rows of pascal's triangle
    row = []
    for i in range(rowNum):
        row.append(comb(rowNum - 1, i)) # functions uses the fact that the rows of pascal's triangle follow the choose numbers

    return row

def main():
    t = turtle.Turtle()
  
    width, height = turtle.screensize()
  
    row = int(input("What row of Pascal's triangle would you like to visualise? Row Number: "))
  
    colWidth = width / row
    colHeightMult = height / pascal(row)[len(pascal(row)) // 2] # calculates a multiplier for the number in the row making it the height, making the middle number(s) just barely fit
  
    t.speed('fastest')
  
    showAnimation = input('Show animation? Y/N: ').upper()
    if showAnimation == 'N':
        turtle.tracer(0,0)
    
    t.pencolor('black')
    t.fillcolor('white')
    turtle.Screen().bgcolor('black')
  
    t.penup()
    t.goto(-(width / 2), -(height / 2)) # goes to the bottom left hand corner
    t.pendown()
    t.left(90)
  
    fontStyle = ('Roboto', int(colWidth//4), 'italic') # font size was trial and error
  
    for i in range(row):
        t.begin_fill()
  
        for _ in range(2):
            t.fd(pascal(row)[i] * colHeightMult)
            t.right(90)
            t.fd(colWidth)
            t.right(90)
        t.end_fill()
  
        if row <= 25: # after 25 numbers get too long and font size is too small to see
            t.penup()
            t.fd(pascal(row)[i] * colHeightMult)
            t.right(90)
            t.fd(colWidth/2)
            t.left(90)
            t.fd(10)
            t.color('white')
            t.write(str(pascal(row)[i]), font=fontStyle, align='center') # writes pascal number above column
            t.pencolor('black')
    
            t.bk(10)
            t.right(90)
            t.fd(colWidth/2)
            t.right(90)
            t.fd(pascal(row)[i]*colHeightMult)
            t.left(180)
            t.pendown()
  
        else:
            t.penup()
            t.right(90)
            t.fd(colWidth)
            t.left(90)
            t.pendown()

    t.color('black') # so you can't see the turtle
    
    if showAnimation == 'N':
        turtle.update()

if __name__ == 'main':
    main()