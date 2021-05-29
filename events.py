"""
https://www.pygame.org/docs/ref/event.html#pygame.event.Event
https://riptutorial.com/pygame/example/18046/event-loop
"""
from os.path import isfile

from random import randint

import pygame as pg  # type: ignore
from pygame.event import Event  # type: ignore
from pygame import mixer

# from pygame import JOYBUTTONDOWN, KEYDOWN, MOUSEBUTTONDOWN, QUIT  # type: ignore

from config import CHANNELS, FORMAT


def playsound(sndFile: str):
    ch = mixer.find_channel()
    snd = mixer.Sound(file=sndFile)
    ch.set_volume(mixer.music.get_volume())
    ch.play(snd)


def bound(v):
    if v > 1:
        return 1
    elif v < 0:
        return 0
    else:
        return v


class Command:
    def exec(self, e: Event):
        print(f"Event: {e}")

    def __repr__(self):
        return str(self.__class__.__name__)


class QuitCommand(Command):
    def exec(self, e: Event):
        super().exec(e)
        pg.quit()
        quit()


class ButtonClickCommand(Command):
    def exec(self, e: Event):
        super().exec(e)
        # pygame.quit()
        print(f"Button: {e.button}")
        fname = f"sounds/{e.button}.{FORMAT}"
        if isfile(fname):
            playsound(fname)
        else:
            print(f"Not found: {fname}")


class KeyClickCommand(Command):
    def exec(self, e: Event):
        super().exec(e)
        print(f"Key: {e.key}")
        fname = f"{e.key}.{FORMAT}"
        if isfile(fname):
            playsound(fname)
        else:
            print(f"Not found: {fname}")


class AdjustCommand(Command):
    def exec(self, e: Event):
        super().exec(e)
        print(f"Axis: {e.axis}")
        if e.axis == 1:
            v = mixer.music.get_volume()
            mixer.music.set_volume(bound(v - 0.1 * e.value))
            print(f"Volume from {v} to {mixer.music.get_volume()}")
        else:
            print(f"Axis not used: {e.axis}")


events_map = {
    pg.JOYAXISMOTION: AdjustCommand(),
    # pg.JOYHATMOTION: QuitCommand(),
    pg.JOYBUTTONDOWN: ButtonClickCommand(),
    pg.KEYDOWN: KeyClickCommand(),
    pg.MOUSEBUTTONDOWN: ButtonClickCommand(),
    pg.QUIT: QuitCommand(),
}
