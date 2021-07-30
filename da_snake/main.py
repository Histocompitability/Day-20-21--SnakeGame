from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
food = Food()
scoreboard = Scoreboard()
scoreboard.write_score(scoreboard.counter_of_a_score)

while game_is_on:
    snake.move()
    if snake.head.distance(food) < 9:
        print("om nom nom")
        scoreboard.counter_of_a_score += 1
        scoreboard.write_score(scoreboard.counter_of_a_score)
        food.refresh()

screen.exitonclick()