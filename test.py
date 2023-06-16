from pynput import keyboard

def handle_key_press(key):
    if key == keyboard.Key.shift_l:
        with keyboard.Controller() as controller:
            controller.type('Does this work')

with keyboard.Listener(on_press=handle_key_press) as listener:
    listener.join()