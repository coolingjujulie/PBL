#Import all the files, be careful here there will be a lot of errors
from Models.animalClass import Monkey
from Models.animalClass import Dog
from Models.animalClass import TurtleRacer
from Models.animalClass import Rabbit
from Models.animalClass import Bird
from Models.ArtefactsClass import Carrot
from Models.ArtefactsClass import Fence
from Models.ArtefactsClass import Lettuce
from Models.ArtefactsClass import Banana
from Models.ArtefactsClass import Bone
from Models.raceTrackClass import RaceTrack
from Models.sound import SoundPlayer



import random


class AnimalRaceGame:
    def __init__(self):
        self.track = RaceTrack(1000, 320)
        self.finish_line = 450

    def play_sound(self):
        self.sound = SoundPlayer()
        self.sound.play_music("sounds/background.mp3")  # música de fondo

    def play_effect(self, file):
        self.sound.play_effect(file)

    def stop_sound(self):
        self.sound.stop_music()


    def create_animals(self):
        positions = [
        (-450, 134),
        (-450, 67),
        (-450, 0),
        (-450, -67),
        (-450, -134)
        ]
        random.shuffle(positions) 
        monkey = Monkey(positions[0])
        bird = Bird(positions[1])
        dog = Dog(positions[2])
        turtle_racer = TurtleRacer(positions[3])
        rabbit = Rabbit(positions[4])
        return monkey, dog, turtle_racer, rabbit, bird


    def create_food_items(self, num_items):
        starting_line = -(self.track.width // 2) + 50
        finish_line = (self.track.width // 2) - 50
        food_classes = [Bone, Lettuce, Banana, Carrot]
        foods = [random.choice(food_classes)((random.randint(starting_line, finish_line), random.choice([134 ,67, 0, -67, -134]))) for _ in range(num_items)]
        return foods
    
    def create_fences(self, num_items):
        starting_line = -(self.track.width // 2) + 50
        finish_line = (self.track.width // 2) - 50
        Fence_classes = [Fence]
        fences = [random.choice(Fence_classes)((random.randint(starting_line, finish_line), random.choice([134 ,67, 0, -67, -134]))) for _ in range(num_items)]
        return fences
