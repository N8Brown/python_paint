from tkinter import *

# GLOBAL VARIABLES


# FUNCTIONS

def paint(event):
    # Starting point of the event
    x1 = event.x - 1
    y1 = event.y - 1
    # Ending point of the event
    x2 = event.x + 1
    y2 = event.y + 2

    canvas.create_line(x1, y1, x2, y2, fill="green", smooth=True)



root = Tk()
root.title("NAB Paint")
root.geometry("800x600")

canvas = Canvas(root, width=600, height=400, bg="white")
canvas.pack(pady=20)

canvas.create_line(0, 200, 800, 200, fill="green")
canvas.create_line(300, 0, 300, 600, fill="green")

canvas.bind('<B1-Motion>', paint)

root.mainloop()