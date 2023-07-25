"""Module provides BRB Message actions"""
import time
from pynput.keyboard import Key, Controller
from threader import Threader

class BRBMessage(Threader):
    """BRB Message Thread"""
    def __init__(self, message, num_dots) -> None:
        super().__init__()
        self.message = message
        self.num_dots = num_dots
        self.name = "BRB Message"

    def run(self):
        keyboard = Controller()
        while self.thread_running:
            while self.running:
                # Type out message
                for i in self.message:
                    if not self.running:
                        break
                    time.sleep(0.25)
                    keyboard.tap(i)
                # Type out dots
                for i in range(self.num_dots):
                    if not self.running:
                        break
                    time.sleep(1.5)
                    keyboard.tap('.')
                time.sleep(1.5)
                # Backspace everything
                for i in range(len(self.message) + self.num_dots):
                    if not self.running:
                        break
                    time.sleep(0.1)
                    keyboard.tap(Key.backspace)
            time.sleep(0.1)
