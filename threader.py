import time
import threading

class Threader(threading.Thread):
    def __init__(self) -> None:
        super(Threader, self).__init__()
        self.running = False
        self.thread_running = True

    def start_typing(self):
        self.running = True
        print(f"✅ Starting {self.name}")

    def stop_typing(self):
        self.running = False
        print(f"🛑 Stopping {self.name}")

    def exit(self):
        self.stop_typing()
        self.thread_running = False
        print(f"👋 Exiting {self.name}")

    def run(self):
        while self.thread_running:
            while self.typing:
                pass
            time.sleep(0.1)