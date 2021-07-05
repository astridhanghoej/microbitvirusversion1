radio.onReceivedNumber(function (receivedNumber) {
    // Only happens if receiving microbit has non-infected status. Otherwise it only transmits in the forever loop.
    // Range -128 to -42. -50 is pretty close to eachother (approx 40cm unshielded). Tweak to transmit at larger distances.
    if (!(isInfected) && radio.receivedPacket(RadioPacketProperty.SignalStrength) > -70) {
        // Tweak to make it more likely to catch the disease
        // 
        // Pick Random: a floating-point, pseudo-random number between 0 (inclusive) and 1 (exclusive).
        if (3 > randint(0, 10)) {
            isInfected = 1
            basic.clearScreen()
            basic.showIcon(IconNames.Skull)
            // Some people who catch it will become audibly sick for a short period of time (just a quick beep). Remove to only work with visual cues.
            if (Math.randomBoolean()) {
                music.playTone(262, music.beat(BeatFraction.Half))
            }
        }
    }
})
// This handle ensures that one or more microbits can be set to patient zero during game play.
input.onButtonPressed(Button.AB, function () {
    isInfected = 1
    basic.clearScreen()
    basic.showIcon(IconNames.Skull)
})
let isInfected = 0
isInfected = 0
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    if (isInfected) {
        radio.sendNumber(isInfected)
    }
    // The virus only transmits every 5 seconds so there is a chance you could be close to someone who is infected and not know it.
    // 
    // Tweak it to make it less visible to people around you.
    control.waitMicros(1000000)
})
