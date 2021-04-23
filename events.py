"""
https://www.pygame.org/docs/ref/event.html#pygame.event.Event
https://riptutorial.com/pygame/example/18046/event-loop
"""
from os.path import isfile

import pygame as pg  # type: ignore
from pygame.event import Event  # type: ignore

from playsound import playsound  # type: ignore

# from pygame import JOYBUTTONDOWN, KEYDOWN, MOUSEBUTTONDOWN, QUIT  # type: ignore


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
        fname = f"sounds/{e.button}.mp3"
        if isfile(fname):
            playsound(fname)
        else:
            print(f"Not found: {fname}")


class KeyClickCommand(Command):
    def exec(self, e: Event):
        super().exec(e)
        print(f"Key: {e.key}")
        fname = f"{e.key}.mp3"
        if isfile(fname):
            playsound(fname)
        else:
            print(f"Not found: {fname}")


events_map = {
    pg.JOYAXISMOTION: QuitCommand(),
    # pg.JOYHATMOTION: QuitCommand(),
    pg.JOYBUTTONDOWN: ButtonClickCommand(),
    pg.KEYDOWN: KeyClickCommand(),
    pg.MOUSEBUTTONDOWN: ButtonClickCommand(),
    pg.QUIT: QuitCommand(),
}
