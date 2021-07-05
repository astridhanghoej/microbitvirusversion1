def on_received_number(receivedNumber):
    global isInfected
    # Only happens if receiving microbit has non-infected status. Otherwise it only transmits in the forever loop.
    # Range -128 to -42. -50 is pretty close to eachother (approx 40cm unshielded). Tweak to transmit at larger distances.
    if not (isInfected) and radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) > -70:
        # Tweak to make it more likely to catch the disease
        # 
        # Pick Random: a floating-point, pseudo-random number between 0 (inclusive) and 1 (exclusive).
        if 3 > randint(0, 10):
            isInfected = 1
            basic.clear_screen()
            basic.show_icon(IconNames.SKULL)
            # Some people who catch it will become audibly sick for a short period of time (just a quick beep). Remove to only work with visual cues.
            if Math.random_boolean():
                music.play_tone(262, music.beat(BeatFraction.HALF))
radio.on_received_number(on_received_number)

# This handle ensures that one or more microbits can be set to patient zero during game play.

def on_button_pressed_ab():
    global isInfected
    isInfected = 1
    basic.clear_screen()
    basic.show_icon(IconNames.SKULL)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

isInfected = 0
isInfected = 0
basic.show_icon(IconNames.HEART)

def on_forever():
    if isInfected:
        radio.send_number(isInfected)
    # The virus only transmits every 5 seconds so there is a chance you could be close to someone who is infected and not know it.
    # 
    # Tweak it to make it less visible to people around you.
    control.wait_micros(1000000)
basic.forever(on_forever)
