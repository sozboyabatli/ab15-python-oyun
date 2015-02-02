# -*- coding:utf-8 -*-

import sfml as sf


pencere = sf.RenderWindow(sf.VideoMode(640, 480),
                          "AB2015 python oyun kursu")


while pencere.is_open:
    for event in pencere.events:

        if type(event) is sf.CloseEvent:
            pencere.close()
        if type(event) is sf.KeyEvent:
            if event.released and event.code is sf.Keyboard.ESCAPE:
                pencere.close()
        if type(event) is sf.MouseMoveEvent:
            print(event.position)

    if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
        pencere.close()
    pencere.clear()
    pencere.display()
