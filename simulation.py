import math
import random
import pygame

import plates
import settings
import three_dimension_functions

class Simulation:
    def __init__(self):
        # Initialize pygame
        pygame.mixer.pre_init()
        pygame.init()

        # Make window
        self.screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.idle_rotating = True
        self.alpha = 0
        self.beta = -0.6
        self.gamma = 1.4

        self.drawing_graticules = True
        self.define_graticules()

    def define_graticules(self):
        self.graticule_locations = []

        hadley_cell = 128
        ferrel_cell = math.floor(0.866 * hadley_cell)
        polar_cell = math.floor(0.5 * hadley_cell)

        for graticule in range(hadley_cell):
            self.graticule_locations.append([0, math.cos(graticule * 2 *  math.pi / hadley_cell), math.sin(graticule * 2 *  math.pi / hadley_cell)])

        for graticule in range(ferrel_cell):
            self.graticule_locations.append([0.5, 0.866 * math.cos(graticule * 2 * math.pi / ferrel_cell), 0.866 * math.sin(graticule * 2 *  math.pi / ferrel_cell)])
            self.graticule_locations.append([-0.5, 0.866 * math.cos(graticule * 2 *  math.pi / ferrel_cell), 0.866 * math.sin(graticule * 2 *  math.pi / ferrel_cell)])

        for graticule in range(polar_cell):
            self.graticule_locations.append([0.866, 0.5 * math.cos(graticule * 2 *  math.pi / polar_cell), 0.5 * math.sin(graticule * 2 *  math.pi / polar_cell)])
            self.graticule_locations.append([-0.866, 0.5 * math.cos(graticule * 2 *  math.pi / polar_cell), 0.5 * math.sin(graticule * 2 *  math.pi / polar_cell)])

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_r:
                    self.alpha = 0
                    self.beta = 0
                    self.gamma = math.pi / 2
                    self.idle_rotating = False

                if event.key == pygame.K_SPACE:
                    self.idle_rotating = not self.idle_rotating

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_w]:
            self.beta += settings.ROTATION_SPEED
        elif pressed_keys[pygame.K_s]:
            self.beta -= settings.ROTATION_SPEED

        if pressed_keys[pygame.K_a]:
            self.alpha += settings.ROTATION_SPEED
        if pressed_keys[pygame.K_d]:
            self.alpha -= settings.ROTATION_SPEED
        
        if pressed_keys[pygame.K_q]:
            self.gamma -= settings.ROTATION_SPEED
        if pressed_keys[pygame.K_e]:
            self.gamma += settings.ROTATION_SPEED


    def update(self):
        if self.idle_rotating:
            self.alpha -= 0.002

    def render(self):
        self.screen.fill(settings.BLACK)
        # Draw Globe
        globe_radius = 700
        self.globe_center = [settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2, 1280]

        globe = three_dimension_functions.project_sphere(globe_radius, self.globe_center)
        pygame.draw.ellipse(self.screen, settings.OCEAN_BLUE, globe)

        # Draw Graticules
        if self.drawing_graticules:
            self.draw_graticules()

        # Draw Continents

    def draw_graticules(self):
        graticule_size = 5
        graticule_radius = 705
        for graticule in self.graticule_locations:
            graticule = [graticule[0] * graticule_radius + self.globe_center[0], graticule[1] * graticule_radius + self.globe_center[1], graticule[2] * graticule_radius + self.globe_center[2]]
            graticule = three_dimension_functions.rotate(graticule, [self.alpha, self.beta, self.gamma], self.globe_center)
            if graticule[2] < 1100:
                graticule = three_dimension_functions.project_sphere(graticule_size, graticule)
                pygame.draw.ellipse(self.screen, settings.SKY_BLUE, graticule)

    def run(self):
        while self.running:
            self.process_input()     
            self.update()
            self.render()
            
            pygame.display.update()
            self.clock.tick(settings.FPS)

        pygame.quit()