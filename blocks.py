from pygame import *

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        #заливка сплошным цветом
        #self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("blocks/platform.png")
        self.rect = sprite.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)