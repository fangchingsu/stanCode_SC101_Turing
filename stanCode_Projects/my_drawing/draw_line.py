"""
File: draw_line.py
Name: Fangching Su
-------------------------
TODO: This program creates lines on an instance of GWindow class.
      There is a circle indicating the user’s first click. A line appears
      at the condition where the circle disappears as the user clicks
      on the canvas for the second time.
"""
# import Class from file
from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# setup window size and title
window = GWindow(title="Draw Line")
# create ball size and color
circle_dot = GOval(20, 20)
circle_dot_s = GOval(16, 16)
# global variable
count_dot = 0
save_x = 0
save_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    # call dot function when mouse clicked
    onmouseclicked(dot)


def dot(mouse):
    """
    use mouse location to find the dot location
    """
    # call global variable
    global count_dot
    global save_x
    global save_y
    # setup dot location and fill the color
    circle_dot.filled = True
    window.add(circle_dot, x=mouse.x - 10, y=mouse.y - 10)
    circle_dot_s.filled = True
    circle_dot_s.fill_color = "white"
    window.add(circle_dot_s, x=mouse.x - 8, y=mouse.y - 8)
    # if dot is even or zero
    if count_dot % 2 == 0:
        # save the odd dot location
        save_x = mouse.x
        save_y = mouse.y
        count_dot += 1
    # else
    else:
        # draw the line
        line = GLine(save_x, save_y, mouse.x, mouse.y)
        window.add(line)
        count_dot += 1
        # remove the second dot of line
        window.remove(circle_dot)
        window.remove(circle_dot_s)


if __name__ == "__main__":
    main()
