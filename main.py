def on_button_pressed_a():
    global nb
    if nb < 10:
        nb += 1
        basic.show_number(nb)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global nb
    if nb >= 10:
        pass
    else:
        nb += 1
        basic.show_number(nb)
input.on_button_pressed(Button.B, on_button_pressed_b)

nb = 0
nb = 1
basic.show_number(nb)

def on_forever():
    pass
basic.forever(on_forever)
