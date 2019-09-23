from microbit import *
import random

score = 0
count = 0
iets = random.randint(1, 2)
while True:
    if iets == 1:
        display.show(Image.ARROW_E)
        if button_a.is_pressed():
            count += 1
            display.show(Image.SAD)
            sleep(2500)
            if count == 10:
                display.show(score)
                break
            iets = random.randint(1, 2)
        elif button_b.is_pressed():
            display.show(Image.HAPPY)
            score += 1
            sleep(2500)
            iets = random.randint(1, 2)

    elif iets == 2:
        display.show(Image.ARROW_W)
        if button_b.is_pressed():
            count += 1
            display.show(Image.SAD)
            sleep(2500)
            if count == 10:
                display.show(score)
                break
            iets = random.randint(1, 2)
        elif button_a.is_pressed():
            display.show(Image.HAPPY)
            score += 1
            sleep(2500)
            iets = random.randint(1, 2)