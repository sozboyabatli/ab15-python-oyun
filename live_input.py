# -*- coding: utf-8 -*-

import sfml as sf

window = sf.RenderWindow(sf.VideoMode(800, 400), "Merhaba")

while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.KeyEvent:
            if event.released and event.code is sf.Keyboard.ESCAPE:
                window.close()
        pos = sf.Mouse.get_position(window)

        if sf.Keyboard.is_key_pressed(sf.Keyboard.SPACE):
            print "Space tuşuna basılıyor"
        if sf.Keyboard.is_key_pressed(sf.Keyboard.M):
            print ("Farenin anlık pozisyonu {0} ".format(pos))
            if sf.Keyboard.is_key_pressed(sf.Keyboard.W):
                print "M ve W birlikte basılıyor"

    window.clear(sf.Color.BLACK)
    window.display()