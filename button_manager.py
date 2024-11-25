import pygame

class ButtonManager:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.buttons = []

    def add_button(self, label, rect, color, callback):
        self.buttons.append({"label": label, "rect": rect, "color": color, "callback": callback})

    def draw_buttons(self):
        # Draw buttons to screen
        for button in self.buttons:
            pygame.draw.rect(self.screen, button["color"], button["rect"])
            label_surface = self.font.render(button["label"], True, (255, 255, 255))
            self.screen.blit(label_surface, (button["rect"].x + 10, button["rect"].y + 10))

    def handle_click(self, mouse_pos):
        # Execute callback if button is clicked
        for button in self.buttons:
            if button["rect"].collidepoint(mouse_pos):
                button["callback"]()
