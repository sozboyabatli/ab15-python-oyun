# -*- coding:utf-8 -*-

import sfml as sf

WIDTH = 800
HEIGHT = 600
TITLE = "ROHAEHOHEY"

window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT),TITLE)

while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.MouseMoveEvent:
            print("Fare hareketlendi.%s" % event.position)
        if type(event) is sf.KeyEvent:
            if event.released and event.code is sf.Keyboard.ESCAPE:
                window.close()
            if not event.released and event.code is sf.Keyboard.W:
                print "W"
    window.clear()
    window.display()