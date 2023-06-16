from pynput import keyboard

controller = keyboard.Controller()

def handle_key_press(key):
    if key in [keyboard.Key.shift_l, keyboard.Key.shift_r]:
        controller.type('This works')

with keyboard.Listener(on_press=handle_key_press) as listener:
    listener.join()
