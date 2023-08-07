"""Module providing a Thread template"""
import threading


class Threader(threading.Thread):
    """Thread Template"""
    def __init__(self) -> None:
        super().__init__()
        self.running = False
        self.thread_running = True

    def start_typing(self):
        """Start action"""
        self.running = True
        print(f"✅ Starting {self.name}")

    def stop_typing(self):
        """Stop action"""
        self.running = False
        print(f"🛑 Stopping {self.name}")

    def exit(self):
        """Exit thread"""
        self.stop_typing()
        self.thread_running = False
        print(f"👋 Exiting {self.name}")
