"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
# import Class from file
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# constant
BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


# create class
class BreakoutGraphics:
    # class constructor
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2, y=window_height - paddle_offset)
        self.paddle_offset = paddle_offset
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - self.ball.width) / 2, y=(window_height - self.ball.height) / 2)
        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners.
        self.switch = True
        onmouseclicked(self.ball_start)
        onmousemoved(self.paddle_move)
        # Draw bricks.
        color = ""
        for j in range(brick_rows):
            for i in range(brick_cols):
                if j == 0 or j == 1:
                    color = "red"
                elif j == 2 or j == 3:
                    color = "orange"
                elif j == 4 or j == 5:
                    color = "yellow"
                elif j == 6 or j == 7:
                    color = "green"
                elif j == 8 or j == 9:
                    color = "blue"
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color
                self.window.add(self.brick, x=i * (brick_spacing + brick_width),
                                y=brick_offset + j * (brick_spacing + brick_height))
        # Create scores label.
        self.score = 0
        self.score_label = GLabel("Scores: " + str(self.score))
        self.score_label.font = "-20"
        self.window.add(self.score_label, 10, 35)
        # Create ball life.
        self.ball_life_1 = GOval(20, 20)
        self.ball_life_1.filled = True
        self.window.add(self.ball_life_1, window_width - 100, 20)
        self.ball_life_2 = GOval(20, 20)
        self.ball_life_2.filled = True
        self.window.add(self.ball_life_2, window_width - 70, 20)
        self.ball_life_3 = GOval(20, 20)
        self.ball_life_3.filled = True
        self.window.add(self.ball_life_3, window_width - 40, 20)

    def ball_start(self, mouse):
        """
        when mouse clicks, start the game, lock the mouse clicked
        """
        if self.switch:
            # lock onmouseclicked
            self.switch = False
            # set ball velocity
            self.set_ball_velocity()

    def paddle_move(self, mouse):
        """
        let paddle moved with mouse
        """
        # set paddle location
        self.paddle.x = mouse.x - self.paddle.width / 2
        # set the paddle location when mouse out of window width
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width

    def set_ball_velocity(self):
        """
        let ball run in random velocity when ball started moved
        """
        # set up dx random velocity in range
        self.__dx = random.randint(1, MAX_X_SPEED)
        # ball had one half chance to run in opposite x direction
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def ball_in_area(self):
        """
        make sure ball in window area
        """
        ball_in_y = self.ball.y < self.window.height - self.ball.height
        return ball_in_y

    def remove_ball(self, lives):
        """
        deduct each ball life when ball out of area in three times
        """
        if lives == 3:
            self.window.remove(self.ball_life_3)
        if lives == 2:
            self.window.remove(self.ball_life_2)
        if lives == 1:
            self.window.remove(self.ball_life_1)

    def move_ball(self):
        """
        ball start to move
        """
        self.ball.move(self.__dx, self.__dy)

    def handle_wall_collisions(self):
        """
        when ball collision on wall
        """
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0 or self.ball.y >= self.window.height - self.ball.height:
            self.__dy = -self.__dy

    def check_collisions(self):
        """
        check ball collided on each side
        remove the brick when ball clicked on it
        ball reverse when clicks on bricks and paddle
        """
        # set up ball's location on each side
        ball_side_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_side_2 = self.window.get_object_at(self.ball.x + 2 * self.ball.width, self.ball.y)
        ball_side_3 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball.height)
        ball_side_4 = self.window.get_object_at(self.ball.x + 2 * self.ball.width, self.ball.y + 2 * self.ball.height)
        # set up ball reverse range
        if ball_side_1 is not None and ball_side_1 is not self.score_label and ball_side_1 is not self.ball_life_1 \
                and ball_side_1 is not self.ball_life_2 and ball_side_1 is not self.ball_life_3:
            # when ball hits the paddle
            if ball_side_1 is self.paddle:
                # reverse ball direction
                self.ball_reverse_p()
            # when ball hits the brick
            else:
                self.window.remove(ball_side_1)
                # add the score
                self.score += 1
                # update in score label
                self.score_label.text = "Scores: " + str(self.score)
                # reverse ball direction
                self.ball_reverse()
        # same as ball_side_1
        elif ball_side_2 is not None and ball_side_2 is not self.score_label and ball_side_2 is not self.ball_life_1 \
                and ball_side_2 is not self.ball_life_2 and ball_side_2 is not self.ball_life_3:
            if ball_side_2 is self.paddle:
                self.ball_reverse_p()
            else:
                self.window.remove(ball_side_2)
                self.score += 1
                self.score_label.text = "Scores: " + str(self.score)
                self.ball_reverse()
        # same as ball_side_1
        elif ball_side_3 is not None and ball_side_3 is not self.score_label and ball_side_3 is not self.ball_life_1 \
                and ball_side_3 is not self.ball_life_2 and ball_side_3 is not self.ball_life_3:
            if ball_side_3 is self.paddle:
                self.ball_reverse_p()
            else:
                self.window.remove(ball_side_3)
                self.score += 1
                self.score_label.text = "Scores: " + str(self.score)
                self.ball_reverse()
        # same as ball_side_1
        elif ball_side_4 is not None and ball_side_4 is not self.score_label and ball_side_4 is not self.ball_life_1 \
                and ball_side_4 is not self.ball_life_2 and ball_side_4 is not self.ball_life_3:
            if ball_side_4 is self.paddle:
                self.ball_reverse_p()
            else:
                self.window.remove(ball_side_4)
                self.score += 1
                self.score_label.text = "Scores: " + str(self.score)
                self.ball_reverse()

    def ball_reverse(self):
        """
        reverse ball direction when ball hits bricks
        """
        self.__dy = -self.__dy

    def ball_reverse_p(self):
        """
        reverse ball direction when ball hits the paddle
        """
        if self.__dy > 0:
            self.__dy = -self.__dy

    def win(self):
        """
        show the message when win
        """
        message = GLabel("YOU WIN!!!", x=self.window.width / 5, y=self.window.height / 2)
        message.font = "-50"
        self.window.add(message)

    def game_over(self):
        """
        show the message when lose
        """
        message = GLabel("GAME OVER!!!", x=self.window.width / 6, y=self.window.height / 2)
        message.font = "-50"
        self.window.add(message)

    def reset_ball(self):
        """
        reset ball position and velocity when restart the game
        """
        self.ball.x = random.randint(0, self.window.width - self.ball.width)
        self.ball.y = random.randint(self.brick.y, self.window.height - 5 * self.paddle.height)
        if self.__dy > 0:
            self.__dy = -self.__dy
