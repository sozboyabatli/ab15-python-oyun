# -*- coding: utf-8

import sfml as sf

WIDTH = 800
HEIGHT = 480
TITLE = "Python sfml class example"

class Game:
    def __init__(self):
        self.window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT), TITLE)

        self.circle = sf.CircleShape(50)
        self.circle.origin = self.circle.radius, self.circle.radius

    def run(self):
        while self.window:
            for event in self.window.events:
                self.handle_events(event)
                self.update()
                self.render()

    def handle_events(self, event):
        if type(event) is sf.CloseEvent:
            self.window.close()

    def render(self):
        self.window.clear()
        self.window.draw(self.circle)
        self.window.display()

    def update(self):
        self.circle.position = sf.Mouse.get_position(self.window)

if __name__ == "__main__":
    oyun = Game()
    oyun.run()
