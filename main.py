basic.show_icon(IconNames.HEART)

def on_forever():
    cuteBot.move_time(cuteBot.Direction.FORWARD, 50, 0.25)
    while cuteBot.ultrasonic(cuteBot.SonarUnit.INCHES) <= 10:
        cuteBot.move_time(cuteBot.Direction.BACKWARD, 50, 0.25)
        cuteBot.move_time(cuteBot.Direction.LEFT, 50, 0.25)
basic.forever(on_forever)
