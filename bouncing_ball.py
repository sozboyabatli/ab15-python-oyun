# -*- coding: utf-8 -*-

import sfml as sf

WIDHT = 800
HEIGHT = 480
TITLE = "Ziplayan top!"
SPEED_FACTOR = 60

settings = sf.ContextSettings()
settings.antialiasing_level = 8

class Ball:
    def __init__(self):
        self.window = sf.RenderWindow(sf.VideoMode(WIDHT, HEIGHT), TITLE, sf.Style.DEFAULT, settings)
        self.window.framerate_limit = 20
        self.circle = sf.CircleShape(50)
        self.circle.origin = self.circle.radius, self.circle.radius
        self.circle.position = self.window.size / 2
        self.c_vel = sf.Vector2(5, 5)
        self.clock = sf.Clock()

    def run(self):
        while self.window.is_open:
            for event in self.window.events:
                self.event_handler(event)

            elapsed_time = self.clock.restart().seconds
            self.update(elapsed_time)
            self.render()

    def update(self, delta):
        self.circle.move(self.c_vel)
        if not self.circle.radius < self.circle.position.y < HEIGHT - self.circle.radius:
            x, y = self.c_vel
            y *= -1.0
            self.c_vel = sf.Vector2(x, y)
        if not self.circle.radius < self.circle.position.x < WIDHT - self.circle.radius:
            x, y = self.c_vel
            x *= -1.0
            self.c_vel = sf.Vector2(x, y)
        self.circle.move(self.c_vel * delta * SPEED_FACTOR)

    def render(self):
        self.window.clear()
        self.window.draw(self.circle)
        self.window.display()

    def event_handler(self, event):
        if type(event) is sf.CloseEvent:
            self.window.close()

if __name__ == "__main__":
    top = Ball()
    top.run()
