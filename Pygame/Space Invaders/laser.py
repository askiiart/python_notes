import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height, color='white'):
        """
        Initializes the Laser class
        :param pos: Position
        :param speed: Speed
        :param screen_height: Screen Height
        :param color: Color
        """
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.y_constraint = screen_height

    def destroy_conditionally(self):
        """
        Destroys Laser when out of bounds in the y dimension
        :return: None
        """
        if self.rect.y <= -50 or self.rect.y >= self.y_constraint + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy_conditionally()
