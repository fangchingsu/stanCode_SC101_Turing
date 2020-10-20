"""
File: bouncing_ball.py
Name: Fangching Su
-------------------------
TODO: This program simulates a bouncing ball at (START_X, START_Y)
      that has VX as x velocity and 0 as y velocity. Each bounce reduces
      y velocity to REDUCE of itself.
"""
# import Class from file
from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
switch = True
# setup window size and title
window = GWindow(800, 500, title='bouncing_ball.py')
# create ball size and color
ball = GOval(SIZE, SIZE)
ball.filled = True
count = 3


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball, x=START_X, y=START_Y)
    # call move function when mouse clicked
    onmouseclicked(move)


def move(mouse):
    """
    let ball start bouncing
    """
    time = 1
    global switch, count
    if switch:
        # block mouse click
        switch = False
        while count > 0:
            # let ball move
            ball.move(VX, time)
            # if ball out of window height
            if ball.y > window.height - SIZE:
                # let ball rebound
                time = -time * REDUCE
                # let ball back to window bottom
                ball.y = window.height - ball.height
            # check ball over window width
            if ball.x > window.width - SIZE:
                # let ball back to original location
                window.add(ball, x=START_X, y=START_Y)
                switch = True
                count -= 1
                # out of loop
                break
            # let ball move in DELAY millisecond
            pause(DELAY)
            # accumulate GRAVITY
            time += GRAVITY


if __name__ == "__main__":
    main()
