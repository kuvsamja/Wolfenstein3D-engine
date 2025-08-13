import pygame
import math

pygame.init()

width = 1024
height = 512
fps = 20

# Player variables
x = 128
y = 256
dx = 0
dy = 0
player_height = 16
player_width = 16
player_speed = 9
player_angle = math.pi
sensitivity = math.pi/8

class DrawRays3D():
    def __init__(self, x, y, player_angle, map_width, map_height, map):
        self.x = x
        self.y = y
        self.map = world_map.map
        self.map_width = map_width
        self.map_height = map_height
        ray_angle = player_angle
        ray_x = x
        ray_y = y
        for r in range(1):
            dof = 0
            aTan = -1/math.tan(ray_angle)
            if ray_angle >  math.pi:
                ray_y = ray_y // 32 * 32
                ray_x = (y - ray_y) * aTan + x
                y_offset = -32
                x_offset = y_offset * aTan
                print("gore")
            if ray_angle < math.pi:
                ray_y = int(ray_y // 32 * 32 + 32)
                ray_x = (y - ray_y) * aTan+x
                y_offset = 32
                x_offset = y_offset * aTan
                print("dole")
            if ray_angle == 0 or ray_angle == math.pi:
                ray_x = x
                ray_y = y
                dof = 16
                print("hor")
            while dof < 16:
                map_x = int(ray_x) // 32
                map_y = int(ray_y) // 32
                map_pos = map_y * self.map_width + map_x
                if(map_pos < map_width * map_height and self.map[map_pos] == 1):
                    dof = 16
                else:
                    ray_x += x_offset
                    ray_y += y_offset
                    dof += 1
            pygame.draw.line(window, GREEN, (x, y), (ray_x, ray_y), 1)


class Map():
    def __init__(self, map_width, map_height, map_unit, pos_x, pos_y):
        self.map_width = map_width
        self.map_height = map_height
        self.map_unit = map_unit
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.map = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
        ]
    def drawMap(self, window):
        self.pos_y = 0
        for i in range(self.map_height):
            for j in range(self.map_width):
                if self.map[i * self.map_width + j] == 1:
                    pygame.draw.rect(window, BLUE, (self.pos_x, self.pos_y, self.map_unit, self.map_unit))
                self.pos_x += self.map_unit
            self.pos_y += self.map_unit
            self.pos_x = 0

def player_movement(player_speed, player_angle):
    tasteri = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if tasteri[pygame.K_w]:
        dx = player_speed * math.cos(player_angle)
        dy = player_speed * math.sin(player_angle)
    if tasteri[pygame.K_s]:
        dx = player_speed * -math.cos(player_angle)
        dy = player_speed * -math.sin(player_angle)
    if tasteri[pygame.K_d]:
        dy = player_speed * math.cos(player_angle)
        dx = player_speed * -math.sin(player_angle)
    if tasteri[pygame.K_a]:
        dy = player_speed * -math.cos(player_angle)
        dx = player_speed * math.sin(player_angle)
    if tasteri[pygame.K_RIGHT]:
        player_angle += sensitivity
        if player_angle > 2 * math.pi:
            player_angle -= 2 * math.pi
    if tasteri[pygame.K_LEFT]:
        player_angle -= sensitivity
        if player_angle <= 0:
            player_angle += 2 * math.pi
            
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
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill(BLACK)
    dx, dy, player_angle = player_movement(player_speed, player_angle)
    world_map = Map(16, 16, 32, 0, 0)
    world_map.drawMap(window)
    draw_rays_3d = DrawRays3D(x, y, player_angle, world_map.map_width, world_map.map_height, world_map.map)

    x += dx
    y += dy
    pygame.draw.rect(window, YELLOW, (x, y, player_width, player_height))
    pygame.draw.line(window, RED, (x + player_width/2, y + player_height/2),
                        ((math.cos(player_angle)*50 + x + player_width/2),
                        (math.sin(player_angle)*50) + y + player_height/2), 2)
    pygame.display.update()
    pygame.time.delay(1000 // fps)
    
pygame.quit()