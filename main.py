"""BRB Message Typer"""
from pynput.keyboard import GlobalHotKeys
from brbmessage import BRBMessage

START_KEY = '<ctrl>+<alt>+h'
STOP_KEY = '<ctrl>+<alt>+i'
MESSAGE = 'Be right back. Brewing coffee'
NUM_DOTS = 10

def main():
    """Main Program"""
    typing_thread = BRBMessage(MESSAGE, NUM_DOTS)
    typing_thread.start()

    def on_start_hotkey():
        if typing_thread.running:
            typing_thread.stop_typing()
        else:
            typing_thread.start_typing()

    def on_stop_hotkey():
        typing_thread.exit()
        listener.stop()

    print(f"Press {START_KEY} key to start/stop")
    print(f"Press {STOP_KEY} key to exit")

    with GlobalHotKeys({
            START_KEY: on_start_hotkey,
            STOP_KEY: on_stop_hotkey}) as listener:
        listener.join()

if __name__ == "__main__":
    main()
