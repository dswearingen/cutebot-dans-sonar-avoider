basic.showIcon(IconNames.Heart)
basic.forever(function () {
    if (cuteBot.ultrasonic(cuteBot.SonarUnit.Inches) <= 10) {
        cuteBot.moveTime(cuteBot.Direction.backward, 50, 0.25)
        cuteBot.moveTime(cuteBot.Direction.left, 50, 0.25)
    } else {
        cuteBot.moveTime(cuteBot.Direction.forward, 50, 0.125)
    }
})
