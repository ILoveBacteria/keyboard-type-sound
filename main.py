from pynput import keyboard
from threading import Thread
import winsound


def beep():
    winsound.Beep(800, 60)


def on_release(_):
    Thread(target=beep).start()


with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
