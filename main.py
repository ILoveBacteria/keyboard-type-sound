from pynput import keyboard
from threading import Thread
from playsound import playsound
import winsound


def beep(key):
    if sound_mode == 0:
        winsound.Beep(800, 60)
    elif sound_mode == 1:
        if key == keyboard.Key.backspace:
            playsound('sounds/backspace.wav')
        elif key == keyboard.Key.enter:
            playsound('sounds/enter.wav')
        else:
            playsound('sounds/keyboard.wav')


def on_release(key):
    Thread(target=beep, args=(key,)).start()


listener = keyboard.Listener(on_release=on_release)
listener.start()
sound_mode = 0
while (True):
    try:
        sound_mode = int(input())
    except ValueError as e:
        print(e)
