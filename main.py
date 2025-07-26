import pygame
import math

pygame.init()

width = 1024
height = 512
fps = 20

# Player variables
x = 256
y = 256
dx = 0
dy = 0
player_height = 16
player_width = 16
player_speed = 9
player_angle = 180
sensitivity = 18


class DrawRays3D():
    def __init__(self, x, y, player_angle, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        ray_angle = player_angle
        ray_x = x
        ray_y = y
        for r in range(1):
            dof = 0
            aTan = -1/math.tan(ray_angle)
            if 90 < ray_angle < 270:
                ray_y = int(ray_y // 64 * 64)
                ray_x = (y - ray_y) * aTan+x
                y_offset = -64
                x_offset = y_offset * aTan
            if ray_angle > 270 or ray_angle < 90:
                ray_y = int(ray_y // 64 * 64 + 64)
                ray_x = (y - ray_y) * aTan+x
                y_offset = 64
                x_offset = y_offset * aTan
            if ray_angle == 90 or ray_angle == 270:
                ray_x = x
                ray_y = y
                dof = 16
            while dof < 16:
                map_x = ray_x // 64
                map_y = ray_y // 64
                map_position = map_y * self.map_width * map_x
                if(map_position < map_width * map_height and map[map_position] == 1):
                    dof = 8
                else:
                    ray_x += x_offset
                    ray_y += y_offset
                    dof += 1
            pygame.draw.line(window, GREEN, (x, y), (ray_x, ray_y), 10)


class Map():
    def __init__(self, map_width, map_height, map_unit, pos_x, pos_y):
        self.map_width = map_width
        self.map_height = map_height
        self.map_unit = map_unit
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.map = [
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        ]
    def drawMap(self, window):
        self.pos_y = 0
        for i in range(self.map_height):
            for j in range(self.map_width):
                if self.map[i][j] == 1:
                    pygame.draw.rect(window, BLUE, (self.pos_x, self.pos_y, self.map_unit, self.map_unit))
                self.pos_x += self.map_unit
            self.pos_y += self.map_unit
            self.pos_x = 0

def player_movement(player_speed, player_angle):
    tasteri = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if tasteri[pygame.K_w]:
        dx = player_speed * math.sin(player_angle * math.pi/180)
        dy = player_speed * math.cos(player_angle * math.pi/180)
    if tasteri[pygame.K_s]:
        dx = player_speed * -math.sin(player_angle * math.pi/180)
        dy = player_speed * -math.cos(player_angle * math.pi/180)
    if tasteri[pygame.K_d]:
        dy = player_speed * math.sin(player_angle * math.pi/180)
        dx = player_speed * -math.cos(player_angle * math.pi/180)
    if tasteri[pygame.K_a]:
        dy = player_speed * -math.sin(player_angle * math.pi/180)
        dx = player_speed * math.cos(player_angle * math.pi/180)
    if tasteri[pygame.K_RIGHT]:
        player_angle -= sensitivity
        if player_angle < 0:
            player_angle += 360
    if tasteri[pygame.K_LEFT]:
        player_angle += sensitivity
        if player_angle > 360:
            player_angle -= 360
            
    return dx, dy, player_angle

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Raycaster")


#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (0, 255, 255)
PURPLE = (100,10,100)

# draw_rays_3d = DrawRays3D()
world_map = Map(16, 16, 32, 0, 0)
draw_rays_3d = DrawRays3D(x, y, player_angle, world_map.map_width, world_map.map_height)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill(BLACK)
    world_map.drawMap(window)
    dx, dy, player_angle = player_movement(player_speed, player_angle)

    x += dx
    y += dy
    pygame.draw.rect(window, YELLOW, (x, y, player_width, player_height))
    pygame.draw.line(window, RED, (x + player_width/2, y + player_height/2),
                        ((math.sin(player_angle * math.pi / 180)*50 + x + player_width/2),
                        (math.cos(player_angle * math.pi / 180)*50 + y + player_height/2)), 2)
    print(player_angle)
    pygame.display.update()
    pygame.time.delay(1000 // fps)
pygame.quit()