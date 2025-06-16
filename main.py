import pygame
from asteroidfield import *
from asteroid import Asteroid
from player import *
from constants import *
from shot import *

def main():

    # Initialize the program
    pygame.init()

    # Player objects, groups and containers
    updateables = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateables, drawable) 
    king_of_trig = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Shots
    bullets = pygame.sprite.Group()
    Shot.containers = (updateables, drawable, bullets)

    #Asteroid objects, groups and containers
    asteroid_cluster = pygame.sprite.Group()
    Asteroid.containers = (asteroid_cluster, updateables, drawable)
    AsteroidField.containers = (updateables) # pyright: ignore
    death_cloud = AsteroidField()

    # Env Objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Env Variables
    dt = 0

    # Console commands letting us know the game launched successfully
    # plus some info about the env
    print(f"Starting Asteroids!\n\nScreen Height: {SCREEN_HEIGHT}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Main game Loop
    while True:

        # Exit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # spawn and refresh screen
        screen.fill("black")
        for image in drawable:
            image.draw(screen)

        updateables.update(dt)

        for asteroid in asteroid_cluster:
            if asteroid.check_collide(king_of_trig):
                print("Game Over!")
                return
            for bullet in bullets:
                if asteroid.check_collide(bullet):
                    asteroid.split()
                    bullet.kill()

        dt = clock.tick(60) / 1000
        
        # END OF LOOP NOTHING AFTER FLIP 
        pygame.display.flip()

if __name__ == "__main__":
    main()

