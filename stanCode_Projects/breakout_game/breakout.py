"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""
# import Class from file
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# constant
FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    # inheritance super class
    graphics = BreakoutGraphics()
    # create variable and get value from Constant
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        # onmouseclicked locked
        if not graphics.switch:
            # ball in window area
            if graphics.ball_in_area():
                # remove ball live when game started each times
                graphics.remove_ball(lives)
                # ball move
                graphics.move_ball()
                # ball collide on wall
                graphics.handle_wall_collisions()
                # check ball collided on each side, reverse ball direction, remove brick
                graphics.check_collisions()
                if graphics.score == 100:
                    # show win message
                    graphics.win()
                    # end the game
                    break
            else:
                # deduct one live
                lives -= 1
                if lives < 1:
                    # show lose message
                    graphics.game_over()
                    # end the game
                    break
                # reset ball position and velocity
                graphics.reset_ball()
                # unlock onmouseclicked
                graphics.switch = True
        # let ball move in FRAME_RATE millisecond
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
