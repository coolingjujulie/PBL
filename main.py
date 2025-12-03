from Controller.animalRaceGame import *
import turtle
import time
from playsound import playsound
import threading

def initialize():

    # Register shapes
    turtle.register_shape("images/dog/dog.gif")
    turtle.register_shape("images/monkey/monkey.gif")
    turtle.register_shape("images/rabbit/rabbit.gif")
    turtle.register_shape("images/turtle/turtle.gif")
    turtle.register_shape("images/bird/bird.gif")
    dog_frames = [
        "images/dog/dog1.gif",
        "images/dog/dog2.gif",
        "images/dog/dog3.gif",
        "images/dog/dog4.gif",
        "images/dog/dog5.gif"
    ]
    for frame in dog_frames:
        turtle.register_shape(frame)
    
    monkey_frames = [
    "images/monkey/monkey1.gif",
    "images/monkey/monkey2.gif",
    "images/monkey/monkey3.gif",
    "images/monkey/monkey4.gif",
    "images/monkey/monkey5.gif"
    ]
    for frame in monkey_frames:
        turtle.register_shape(frame)


    rabbit_frames = [
        "images/rabbit/rabbit1.gif",
        "images/rabbit/rabbit2.gif",
        "images/rabbit/rabbit3.gif",
        "images/rabbit/rabbit4.gif",
        "images/rabbit/rabbit5.gif"
        ]
    for frame in rabbit_frames:
        turtle.register_shape(frame)
    
    bird_frames = [
        "images/bird/bird1.gif",
        "images/bird/bird2.gif",
        "images/bird/bird3.gif",
        "images/bird/bird4.gif",
        "images/bird/bird5.gif"
    ]
    for frame in bird_frames:
        turtle.register_shape(frame)

    turtle_frames = [
        "images/turtle/turtle1.gif",
        "images/turtle/turtle2.gif",
        "images/turtle/turtle3.gif",
        "images/turtle/turtle4.gif",
        "images/turtle/turtle5.gif"
    ]
    for frame in turtle_frames:
        turtle.register_shape(frame)



    turtle.register_shape("images/banana.gif")
    turtle.register_shape("images/bone.gif")
    turtle.register_shape("images/lettuce.gif")
    turtle.register_shape("images/carrot.gif")
    turtle.register_shape("images/barrier.gif")
    
    
    game = AnimalRaceGame()
    game.track.create_random_areas(4, ["light green", "light blue"])
    game.track.draw_lanes()
    game.track.create_finish_line()
    fences = game.create_fences(3)
    foods = game.create_food_items(6)
    monkey, dog, turtle_racer, rabbit, bird = game.create_animals()
    dog.animate()
    rabbit.animate()
    monkey.animate()
    bird.animate()
    turtle_racer.animate()
    game.play_sound()
    

    
    
    
    while monkey.get_position()[0] < game.finish_line and dog.get_position()[0] < game.finish_line and turtle_racer.get_position()[0] < game.finish_line and rabbit.get_position()[0] < game.finish_line and bird.get_position()[0] < game.finish_line:
        monkey.move(game.track)
        dog.move(game.track)
        turtle_racer.move(game.track)
        rabbit.move(game.track)
        bird.move(game.track)
        #print("mono", monkey.speed,"perro",dog.speed,"tortuga",turtle_racer.speed,"conejo",rabbit.speed,"pajaro",bird.speed)
        #print("Mono-color", monkey.last_color,"perro-color",dog.last_color,"tortuga-color",turtle_racer.last_color,"conejo-color",rabbit.last_color,"pajaro-color",bird.last_color)

        current_time = time.time()

        if hasattr(monkey, "power_end_time") and current_time >= monkey.power_end_time:
            monkey.restore_speed()
            monkey.power_end_time = float('inf') 

        if hasattr(dog, "power_end_time") and current_time >= dog.power_end_time:
            dog.restore_speed()
            dog.power_end_time = float('inf')

        if hasattr(turtle_racer, "power_end_time") and current_time >= turtle_racer.power_end_time:
            turtle_racer.restore_speed()
            turtle_racer.power_end_time = float('inf')

        if hasattr(rabbit, "power_end_time") and current_time >= rabbit.power_end_time:
            rabbit.restore_speed()
            rabbit.power_end_time = float('inf')


        for food in foods:
            if isinstance(food, Banana) and abs(monkey.get_position()[0] - food.get_position()[0]) < 10 and abs(monkey.get_position()[1] - food.get_position()[1]) < 10:
                monkey.double_speed()
                monkey.power_end_time = time.time() + 1 
                food.hide()
                foods.remove(food)
                game.play_effect("sounds/eat.mp3")
                break

            if isinstance(food, Bone) and abs(dog.get_position()[0] - food.get_position()[0]) < 10 and abs(dog.get_position()[1] - food.get_position()[1]) < 10:
                dog.double_speed()
                dog.power_end_time = time.time() + 1
                food.hide()
                foods.remove(food)
                game.play_effect("sounds/eat.mp3")
                break

            if isinstance(food, Lettuce) and abs(turtle_racer.get_position()[0] - food.get_position()[0]) < 10 and abs(turtle_racer.get_position()[1] - food.get_position()[1]) < 10:
                turtle_racer.double_speed()
                turtle_racer.power_end_time = time.time() + 1
                food.hide()
                foods.remove(food)
                game.play_effect("sounds/eat.mp3")
                break

            if isinstance(food, Carrot) and abs(rabbit.get_position()[0] - food.get_position()[0]) < 10 and abs(rabbit.get_position()[1] - food.get_position()[1]) < 10:
                rabbit.double_speed()
                rabbit.power_end_time = time.time() + 1
                food.hide()
                foods.remove(food)
                game.play_effect("sounds/eat.mp3")
                break

        for fence in fences:
            if isinstance(fence, Fence) and abs(rabbit.get_position()[0] - fence.get_position()[0]) < 10 and abs(rabbit.get_position()[1] - fence.get_position()[1]) < 10:
                rabbit.divide_speed()
                rabbit.power_end_time = time.time() + 1
                fences.remove(fence)
                game.play_effect("sounds/hit.mp3")
                break

            if isinstance(fence, Fence) and abs(monkey.get_position()[0] - fence.get_position()[0]) < 10 and abs(monkey.get_position()[1] - fence.get_position()[1]) < 10:
                monkey.divide_speed()
                monkey.power_end_time = time.time() + 1
                fences.remove(fence)
                game.play_effect("sounds/hit.mp3")
                break

            if isinstance(fence, Fence) and abs(dog.get_position()[0] - fence.get_position()[0]) < 10 and abs(dog.get_position()[1] - fence.get_position()[1]) < 10:
                dog.divide_speed()
                dog.power_end_time = time.time() + 1
                fences.remove(fence)
                game.play_effect("sounds/hit.mp3")
                break

            if isinstance(fence, Fence) and abs(turtle_racer.get_position()[0] - fence.get_position()[0]) < 10 and abs(turtle_racer.get_position()[1] - fence.get_position()[1]) < 10:
                turtle_racer.nerf_speed()
                turtle_racer.power_end_time = time.time() + 1
                fences.remove(fence)
                game.play_effect("sounds/hit.mp3")
                break


    winners = []
    if monkey.get_position()[0] >= game.finish_line:
        winners.append("Monkey")
        game.stop_sound()              
        game.play_effect("sounds/win.mp3")
    if dog.get_position()[0] >= game.finish_line:
        winners.append("Dog")
        game.stop_sound()              
        game.play_effect("sounds/win.mp3")
    if turtle_racer.get_position()[0] >= game.finish_line:
        winners.append("Turtle")
        game.stop_sound()              
        game.play_effect("sounds/win.mp3")
    if rabbit.get_position()[0] >= game.finish_line:
        winners.append("Rabbit")
        game.stop_sound()              
        game.play_effect("sounds/win.mp3")
    if bird.get_position()[0] >= game.finish_line:
        winners.append("Bird")
        game.stop_sound()              
        game.play_effect("sounds/win.mp3")


    if len(winners) > 1:
        display_text = "It's a tie between: " + ", ".join(winners)
        game.stop_sound()              
        game.play_effect("sounds/win.mp3")
    else:
        display_text = f"The winner is: {winners[0]}"

    # Display the winner in the window
    winner_turtle = turtle.Turtle()
    winner_turtle.penup()
    winner_turtle.hideturtle()
    winner_turtle.goto(0, 0)
    winner_turtle.write(display_text, align="center", font=("Arial", 24, "normal"))

    turtle.done()



if __name__ == "__main__":
    initialize()