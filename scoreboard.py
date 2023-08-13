from turtle import Turtle


class Scoreboard(Turtle):
    ALIGNMENT = "center"
    FONT = ("Courier", 15, "normal")
    GAME_OVER = "GAME OVER"

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 270)
        self.write(f"Level: {self.level}", align="left", font=Scoreboard.FONT)

    def increase_level(self):
        self.level +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(Scoreboard.GAME_OVER, align="center", font=("Courier", 80, "normal"))