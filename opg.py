# -*- coding:utf-8 -*-

import sfml as sf

WIDTH = 800
HEIGHT = 480
TITLE = "AB2015 Python Oyun Kursu - Tappy Plane"

pencere = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT),TITLE)

cember = sf.CircleShape(150)
cember.fill_color = sf.Color.WHITE

#cember.position = sf.Vector2(100.0, 100.0)

cember.origin = cember.radius, cember.radius
dikdortgen = sf.RectangleShape(sf.Vector2(150, 200))

#x.pos = (123, 123) alttakinin alternarifi
#sf.Vector2(123,123)  Bütün matematiksel ifadeleri destekler

dikdortgen.fill_color = sf.Color.BLUE
dikdortgen.outline_thickness = 2
dikdortgen.outline_color = sf.Color.GREEN
#dikdortgen.rotate(15)

while pencere.is_open:
    for event in pencere.events:
        if type(event) is sf.CloseEvent:
            pencere.close()
        if type(event) is sf.KeyEvent:
            if event.released and event.code is sf.Keyboard.ESCAPE:
                pencere.close()
            if event.released and event.code is sf.Keyboard.W:
                cember.point_count +=1

            if event.released and event.code is sf.Keyboard.S:
                cember.point_count -=1


    cember.position = sf.Mouse.get_position(pencere)
    dikdortgen.position = sf.Mouse.get_position(pencere)

    pencere.clear()

    #pencere.draw(cember)
    pencere.draw(dikdortgen)

    pencere.display()
