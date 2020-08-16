def on_received_number(receivedNumber):
    if receivedNumber == numberA:
        radio.send_string("RightGuess")
    elif receivedNumber == numberA - 1 or receivedNumber == numberA + 1:
        radio.send_string("Warm")
    elif receivedNumber == numberA - 2 or receivedNumber == numberA + 2:
        radio.send_string("Lukewarm")
    else:
        radio.send_string("Cold")
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global numberA, guessA
    if numberselection:
        numberA += 1
    if guessing:
        guessA += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    global guessA, guessing
    if receivedString == "MakeGuess":
        basic.show_string("G")
        guessA = 0
        guessing = True
    elif receivedString == "RightGuess":
        basic.show_icon(IconNames.HAPPY)
        music.play_melody("C D E F G A B C5 ", 250)
        radio.send_string("GameOver")
    elif receivedString == "GameOver":
        basic.show_icon(IconNames.NO)
        guessing = False
    elif receivedString == "Warm":
        basic.show_icon(IconNames.FABULOUS)
        radio.send_string("MakeGuess")
    elif receivedString == "Lukewarm":
        basic.show_icon(IconNames.ASLEEP)
        radio.send_string("MakeGuess")
    elif receivedString == "Cold":
        basic.show_icon(IconNames.SAD)
        radio.send_string("MakeGuess")
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global numberselection, guessing
    if numberselection:
        numberselection = False
        radio.send_string("Select")
    if guessing:
        guessing = False
        radio.send_number(guessA)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

guessA = 0
numberA = 0
guessing = False
numberselection = False
numberselection = True
guessing = False

def on_forever():
    pass
basic.forever(on_forever)
