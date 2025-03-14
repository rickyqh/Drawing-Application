import json
import turtle
def load_config(filename):
    with open(filename,'r') as file:
        return json.load(file)
    
def draw_shape(t,shape_info):
    t.penup()
    t.goto(shape_info['position'][0],shape_info['position'][1])
    t.pendown()
    t.color(shape_info['color'])

    if shape_info['shape'] == 'square':
        t.begin_fill()
        for _ in range(4):
            t.forward(shape_info['size'])
            t.right(90)
        t.end_fill()
    elif shape_info['shape'] == 'triangle':
        t.begin_fill()
        for _ in range(3):
            t.forward(shape_info['size'])
            t.left(120)
        t.end_fill()
    elif shape_info['shape'] == 'rectangle':
        t.begin_fill()
        for _ in range(2):
            t.forward(shape_info['size'][0])
            t.right(90)
            t.forward(shape_info['size'][1])
            t.right(90)
        t.end_fill()
    elif shape_info['shape'] == 'circle':
       t.begin_fill()
       t.circle(shape_info['size'])
       t.end_fill()


def main():
    screen = turtle.getscreen()
    screen.title("draw something")
    screen.bgcolor('brown')
    shapes=load_config('shapes.json')
    t=turtle.getturtle()
    t.speed(0)
    for shape in shapes:
        draw_shape(t,shape)
    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
