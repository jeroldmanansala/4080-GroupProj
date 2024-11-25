import random
import pygame
from drawing_utils import random_position_and_scale, normalize_drawing


class SketchObject:

    def __init__(self, obj_type, dataset, screen):
        self.type = obj_type
        self.drawing = random.choice(dataset)["drawing"]
        self.screen = screen
        self.position, self.scale = random_position_and_scale(800, 600)

    def draw(self):
        # Draw sketch to screen
        drawing = normalize_drawing(self.drawing, target_size=(300 * self.scale, 300 * self.scale))
        for stroke in drawing:
            points = [(x + self.position[0], y + self.position[1]) for x, y in zip(stroke[0], stroke[1])]
            if len(points) > 1:
                pygame.draw.lines(self.screen, (0, 0, 0), False, points, 2)

    def is_clicked(self, mouse_pos):
        # Check if sketch is clicked
        x, y = self.position
        return x <= mouse_pos[0] <= x + 300 * self.scale and y <= mouse_pos[1] <= y + 300 * self.scale

    def get_offset(self, mouse_pos):
        # Calculate offset from mouse position to the top left corner
        return mouse_pos[0] - self.position[0], mouse_pos[1] - self.position[1]

    def update_position(self, mouse_pos, offset_x, offset_y):
        # Update position of sketch
        self.position = (mouse_pos[0] - offset_x, mouse_pos[1] - offset_y)
