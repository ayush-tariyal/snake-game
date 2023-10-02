from turtle import Turtle


FONT = ("Rockwell", 20, "bold")
FONT_COLOR = "cyan4"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\HP\Desktop\Python\Snake Game\data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.color(FONT_COLOR)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(
                r"C:\Users\HP\Desktop\Python\Snake Game\data.txt", mode="w"
            ) as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def new_scoreboard(self):
        self.score += 1
        self.update_scoreboard()
