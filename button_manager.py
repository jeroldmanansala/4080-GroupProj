import pygame

class ButtonManager:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.buttons = []

    def add_button(self, text, rect, color, action):
        self.buttons.append({"text": text, "rect": rect, "color": color, "action": action})

    def draw_buttons(self):
        for button in self.buttons:
            # Draw the rounded rectangle
            pygame.draw.rect(self.screen, button["color"], button["rect"], border_radius=10)  # Adjust border_radius as needed
            
            # Draw the text
            text_surface = self.font.render(button["text"], True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=button["rect"].center)
            self.screen.blit(text_surface, text_rect)

    def handle_click(self, mouse_pos):
        for button in self.buttons:
            if button["rect"].collidepoint(mouse_pos):
                button["action"]()