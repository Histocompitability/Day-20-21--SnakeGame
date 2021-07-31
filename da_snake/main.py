from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from da_snake.boundrees import boundary

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
boundary()

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
    xcord = snake.head.xcor()
    ycord = snake.head.ycor()

    # food collision
    if snake.head.distance(food) < 9:
        print("om nom nom")
        scoreboard.counter_of_a_score += 1
        scoreboard.write_score(scoreboard.counter_of_a_score)
        food.refresh()
        snake.extend_snake()

    # detect collision with a wall
    if xcord >= 280 or xcord <= -280 or ycord >= 280 or ycord <= -280:
        screen.update()
        game_is_on = False
        scoreboard.game_over()

    #detect collision with a tail
    for segment in snake.block_bank[1:]:
        if segment.distance(snake.head) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
