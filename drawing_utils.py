import ndjson
import random


def load_data(file_path):
    with open(file_path, 'r') as f: # Get quickdraw data
        return ndjson.load(f)

def normalize_drawing(drawing, target_size=(300, 300), padding=20): # Normalize sketch to fit while preserving original ratio
    
    all_x = [x for stroke in drawing for x in stroke[0]] # Flatten coordinates from strokes
    all_y = [y for stroke in drawing for y in stroke[1]]

    min_x, max_x = min(all_x), max(all_x) # Get min and max values 
    min_y, max_y = min(all_y), max(all_y)

    # Calculate scale to fit sketch in target size
    scale = min( 
        (target_size[0] - padding * 2) / (max_x - min_x),
        (target_size[1] - padding * 2) / (max_y - min_y)
    )

    return [
        [
            [(x - min_x) * scale + padding for x in stroke[0]], # Normalize x and y coordinates
            [(y - min_y) * scale + padding for y in stroke[1]]
        ]
        for stroke in drawing
    ]

def random_position_and_scale(scene_width, scene_height, padding=50):
    # Generate random coordinates to place sketches within padding
    x = random.randint(padding, scene_width - 300 - padding)
    y = random.randint(padding, scene_height - 300 - padding)

    scale = random.uniform(0.8, 1.2) # Random scale to add variation in sketches
    
    return (x, y), scale
