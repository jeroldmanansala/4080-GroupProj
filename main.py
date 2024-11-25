import pygame
from button_manager import ButtonManager
from sketch_object import SketchObject
from drawing_utils import load_data

# Initialize Pygame and constants
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Scene Creator")
font = pygame.font.SysFont(None, 24)

# Load datasets
tree_data = load_data("tree.ndjson")
house_data = load_data("house.ndjson")

# Initialize UI
button_manager = ButtonManager(screen, font)

# Store all sketches in the scene
sketches = []

# Functions for adding sketches
def add_tree():
    tree = SketchObject("tree", tree_data, screen)
    sketches.append(tree)

def add_house():
    house = SketchObject("house", house_data, screen)
    sketches.append(house)

# Add buttons
button_manager.add_button("Add Tree", pygame.Rect(10, 10, 120, 40), (100, 200, 100), add_tree)
button_manager.add_button("Add House", pygame.Rect(140, 10, 120, 40), (100, 100, 200), add_house)

# Reset scene
def reset_scene():
    sketches.clear()
    tree = SketchObject("tree", tree_data, screen)
    house = SketchObject("house", house_data, screen)
    sketches.extend([tree, house])

reset_scene()

# Main loop
running = True
dragging_object = None
offset_x, offset_y = 0, 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            button_manager.handle_click(mouse_pos)
            for obj in reversed(sketches):  # Topmost object first
                if obj.is_clicked(mouse_pos):
                    dragging_object = obj
                    offset_x, offset_y = obj.get_offset(mouse_pos)
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_object = None
        elif event.type == pygame.MOUSEMOTION and dragging_object:
            dragging_object.update_position(event.pos, offset_x, offset_y)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reset_scene()

    # Clear screen
    screen.fill((220, 240, 255))

    # Draw buttons and sketches
    button_manager.draw_buttons()
    for obj in sketches:
        obj.draw()

    pygame.display.flip()

pygame.quit()
