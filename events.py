"""
https://www.pygame.org/docs/ref/event.html#pygame.event.Event
https://riptutorial.com/pygame/example/18046/event-loop
"""
import pygame as pg  # type: ignore
from pygame.event import Event  # type: ignore
from pygame import mixer

from pygame import K_ESCAPE

# from pygame import JOYBUTTONDOWN, KEYDOWN, MOUSEBUTTONDOWN, QUIT  # type: ignore

from config import SOUND_COUNT

from util import playsound, bound


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
        playsound(e.button)


class KeyClickCommand(Command):
    def exec(self, e: Event):
        super().exec(e)
        print(f"Key: {e.key}")
        if e.key == K_ESCAPE:
            # pg.quit()
            # exit(0)
            QuitCommand().exec(e)
        playsound(e.key % SOUND_COUNT)


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
