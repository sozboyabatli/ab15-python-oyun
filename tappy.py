# -*- coding:utf-8 -*-
import sfml as sf
import sys

WIDTH = 800
HEIGHT = 480
TITLE = "AB2015 Python Oyun Kursu - Tappy Plane"
GRAVITY = 0.0, 0.1

window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT),TITLE)

try:
    bg_texture = sf.Texture.from_file('assets/images/background.png')
    plane_texture = sf.Texture.from_file('assets/images/bart.png')
    s_buffer = sf.SoundBuffer.from_file('assets/sounds/tone1.ogg')
    music = sf.Music.from_file('assets/sounds/spaceTrash3.ogg')
    font = sf.Font.from_file('assets/fonts/kenvector_future_thin.ttf')
except IOError:
    print "Hata"
    sys.exit(-1)

background = sf.Sprite(bg_texture)
plane = sf.Sprite(plane_texture)
plane.position = 300, 20
plane_vel = sf.Vector2(0.0, 0.0)
sound = sf.Sound(s_buffer)
music.loop = True
music.play()

yazi = sf.Text("BART")
yazi.font = font
yazi.character_size = 25
yazi.position = 0.0, 0.0
yazi.color = sf.Color.RED

count = 0
#plane.origin = plane.global_bounds.width / 2, plane.global_bounds.height / 2

while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.KeyEvent:
            if event.released and event.code is sf.Keyboard.ESCAPE:
                window.close()
            if event.released and event.code is sf.Keyboard.SPACE:
                sound.play()
            if event.released and event.code is sf.Keyboard.UP:
                count += 1
                yazi.string = "BART - {0}".format(count)
            if event.released and event.code is sf.Keyboard.DOWN:
                count -= 1
                yazi.string = "BART - {0}".format(count)

    plane_vel += GRAVITY
    plane.move(plane_vel)


    window.clear()
    window.draw(background)
    window.draw(plane)
    window.draw(yazi)
    window.display()

