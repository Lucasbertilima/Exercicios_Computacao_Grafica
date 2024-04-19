import pygame
import sys
from pygame.locals import *
import math


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Desenhar Cubo em Pygame")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


vertices = [
    (-1, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1)
]


faces = [
    (0, 1, 5, 4),  # Face frontal
    (1, 2, 6, 5),  # Face direita
    (2, 3, 7, 6),  # Face traseira
    (3, 0, 4, 7),  # Face esquerda
    (0, 1, 2, 3),  # Face superior
    (4, 5, 6, 7)   # Face inferior
]


def project(vertex):
    x, y, z = vertex
    fov = 256
    distance = 5
    scale = fov / (z + distance)
    screen_x = WIDTH // 2 + int(x * scale)
    screen_y = HEIGHT // 2 + int(y * scale)
    return (screen_x, screen_y)


def draw_cube():
    for face in faces:
        pointlist = [project(vertices[vertex]) for vertex in face]
        pygame.draw.polygon(screen, (255, 255, 255), pointlist)


def rotate_camera(angle_x, angle_y):
    global vertices
    new_vertices = []
    for vertex in vertices:
        x = vertex[0]
        y = vertex[1]
        z = vertex[2]
        new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
        new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
        x = new_x
        z = new_z

        new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
        new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
        y = new_y
        z = new_z
        new_vertices.append((x, y, z))
    vertices = new_vertices


def reset_camera():
    global angle_x, angle_y, rotation_speed
    angle_x = 0
    angle_y = 0
    rotation_speed = 0.000005


angle_x = 0
angle_y = 0
rotation_speed = 0.000005  
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  
                reset_camera()

    
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        angle_y += rotation_speed
    if keys[K_RIGHT]:
        angle_y -= rotation_speed
    if keys[K_UP]:
        angle_x += rotation_speed
    if keys[K_DOWN]:
        angle_x -= rotation_speed

    
    screen.fill(BLACK)

    
    rotate_camera(angle_x, angle_y)

    
    draw_cube()

    
    pygame.display.flip()


pygame.quit()
sys.exit()
