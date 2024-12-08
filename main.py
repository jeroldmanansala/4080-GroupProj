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
dog_data = load_data("dog.ndjson")

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

def add_dog():
    dog = SketchObject("dog", dog_data, screen)
    sketches.append(dog)

# Reset scene
def reset_scene():
    sketches.clear()

# Add buttons
button_manager.add_button("Add Tree", pygame.Rect(10, 10, 120, 40), (100, 200, 100), add_tree)
button_manager.add_button("Add House", pygame.Rect(140, 10, 120, 40), (100, 100, 200), add_house)
button_manager.add_button("Add Dog", pygame.Rect(270, 10, 120, 40), (70, 103, 248), add_dog)


# Calculate position for the right-aligned "Reset" button
reset_button_width = 120
reset_button_height = 40
reset_button_x = width - reset_button_width - 10  # 10px padding from the right edge
reset_button_y = 10  # Same vertical position as before

# Add the button to the ButtonManager
button_manager.add_button("Reset", pygame.Rect(reset_button_x, reset_button_y, reset_button_width, reset_button_height), (255, 120, 120), reset_scene)


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
    screen.fill((255, 255, 255))

    # Draw buttons and sketches
    button_manager.draw_buttons()
    for obj in sketches:
        obj.draw()

    pygame.display.flip()

pygame.quit()
