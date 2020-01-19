from pygame import mixer

mixer.init()

mixer.music.load('money.mp3')
mixer.music.play()

while 1:
    if mixer.get_busy() == 0:
        mixer.music.play()