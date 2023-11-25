from gpiozero import Button
button = Button(2)

count = 0
while True:
    button.wait_for_press()
    print(count)
    count += 1