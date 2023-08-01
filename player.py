from turtle import Turtle


class Player(Turtle):

    STARTING_POSITION = (0, -280)
    MOVE_DISTANCE = 10
    FINISH_LINE = 280

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.initial_position()

    def go_up(self):
        self.forward(Player.MOVE_DISTANCE)

    # def get_player_position_x(self):
    #     return self.xcor()
    #
    # def get_player_position_y(self):
    #     return self.ycor()

    def has_reach_finish_line(self):
        return Player.FINISH_LINE - self.ycor() < 20

    def initial_position(self):
        self.goto(Player.STARTING_POSITION)