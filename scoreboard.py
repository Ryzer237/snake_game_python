from turtle import Turtle
ALIGNMENT="center"
FONT=("arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:

            self.high_score = int(file.read())
        self.score=0

        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.write(f"score:{self.score } high score:{self.high_score}",align=ALIGNMENT,font=FONT)
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
        self.score=0
        self.update_score()

    def increase(self):
        self.score+=1

        self.update_score()