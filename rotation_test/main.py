import pygame
import math

from controllablePoint import ControllablePoint 


# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Sprite's initial position and target position
position = ControllablePoint(300,300, BLUE)
target = ControllablePoint(500,300, RED)
controllables = [position, target]


# ... other code to draw the sprite and handle events ...

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                for c in controllables:
                    c.drag(event.pos[0], event.pos[1])

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                for c in controllables:
                    c.drop(event.pos[0], event.pos[1])

        elif event.type == pygame.MOUSEMOTION:
            for c in controllables:
                c.move(event.pos[0], event.pos[1])
    # ... (Your sprite drawing code) ...
    screen.fill((0, 0, 0))  # Clear the screen

    position.display(screen)
    target.display(screen)

    for rect in controllables:
        rect.display(screen)    


    # Calculate the direction vector
    direction_x = target.x - position.x
    direction_y = target.y - position.y
    # Calculate the angle in radians
    angle_radians = math.atan2(direction_y, direction_x)
    # Calculate the angle in degrees
    angle_degrees = math.degrees(angle_radians)
    # (Optional) Normalize the vector (make its length 1)
    length = math.sqrt(direction_x**2 + direction_y**2)
    normalized_direction_x = direction_x / length
    normalized_direction_y = direction_y / length


    # display sprite with orientation
    image = pygame.image.load('player111.png')
    rotated_image = pygame.transform.rotate(image, -angle_degrees)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = (10,10)).center)
    screen.blit(rotated_image, new_rect)
    
    # Display the angle
    font = pygame.font.Font(None, 30)
    text = font.render(f"Angle: {angle_degrees:.2f} degrees", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
