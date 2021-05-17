from tkinter import *
from tkinter import colorchooser
import tkinter.ttk as ttk

# GLOBAL VARIABLES
brush_color = 'black'

# FUNCTIONS

def paint(event):
    # Starting point of the event
    x1 = event.x - 1
    y1 = event.y - 1
    # Ending point of the event
    x2 = event.x + 1
    y2 = event.y + 1

    canvas.create_line(x1, y1, x2, y2, fill=brush_color, width='%0.0f' % float(brush_size_slider.get()), capstyle=brush_type_choice.get(), smooth=True)


def change_brush_size(x):
    brush_size_label.config(text='%0.0f' % float(brush_size_slider.get()))


def change_brush_color():
    global brush_color
    brush_color = colorchooser.askcolor(color=brush_color)[1]


def change_canvas_color():
    canvas.config(bg=colorchooser.askcolor(color='white')[1])


# APP WINDOW
root = Tk()
root.title("NAB Paint")
root.geometry("800x675")

# Paint canvas where user will paint images 
canvas = Canvas(root, width=600, height=400, bg="white")
canvas.pack(pady=20)
canvas.bind('<B1-Motion>', paint)

# Controls frame to house the brush controls
controls_frame = Frame(root)
controls_frame.pack(pady=20)

# Brush size controls
brush_size_frame = LabelFrame(controls_frame, text="Brush Size")
brush_size_frame.grid(row=0, column=0)
brush_size_slider = ttk.Scale(brush_size_frame, from_=100, to=1, orient=VERTICAL, value=10, command=change_brush_size)
brush_size_slider.pack(pady=10, padx=10)
brush_size_label = Label(brush_size_frame, text=brush_size_slider.get())
brush_size_label.pack(pady=10)

# Brush type controls
brush_type_choice = StringVar()
brush_type_choice.set("round")

brush_type_frame = LabelFrame(controls_frame, text="Brush Type")
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type_radio1 = Radiobutton(brush_type_frame, text="Round", variable=brush_type_choice, value="round")
brush_type_radio1.pack(anchor=W)
brush_type_radio2 = Radiobutton(brush_type_frame, text="Flat", variable=brush_type_choice, value="butt")
brush_type_radio2.pack(anchor=W)
brush_type_radio3 = Radiobutton(brush_type_frame, text="Diamond", variable=brush_type_choice, value="projecting")
brush_type_radio3.pack(anchor=W)

# Brush and canvas color controls
color_frame = LabelFrame(controls_frame, text="Colors")
color_frame.grid(row=0, column=2)

brush_color_button = Button(color_frame, text="Brush Color", command=change_brush_color)
brush_color_button.pack(padx=10, pady=10)

canvas_color_button = Button(color_frame, text="Canvas Color", command=change_canvas_color)
canvas_color_button.pack(padx=10, pady=10)





root.mainloop()