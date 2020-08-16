radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == numberA) {
        radio.sendString("RightGuess")
    } else if (receivedNumber == numberA - 1 || receivedNumber == numberA + 1) {
        radio.sendString("Warm")
    } else if (receivedNumber == numberA - 2 || receivedNumber == numberA + 2) {
        radio.sendString("Lukewarm")
    } else {
        radio.sendString("Cold")
    }
})
input.onButtonPressed(Button.A, function () {
    if (numberselection) {
        numberA += 1
    }
    if (guessing) {
        guessA += 1
    }
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "MakeGuess") {
        basic.showString("G")
        guessA = 0
        guessing = true
    } else if (receivedString == "RightGuess") {
        basic.showIcon(IconNames.Happy)
        music.playMelody("C D E F G A B C5 ", 250)
        radio.sendString("GameOver")
    } else if (receivedString == "GameOver") {
        basic.showIcon(IconNames.No)
        guessing = false
    } else if (receivedString == "Warm") {
        basic.showIcon(IconNames.Fabulous)
        radio.sendString("MakeGuess")
    } else if (receivedString == "Lukewarm") {
        basic.showIcon(IconNames.Asleep)
        radio.sendString("MakeGuess")
    } else if (receivedString == "Cold") {
        basic.showIcon(IconNames.Sad)
        radio.sendString("MakeGuess")
    }
})
input.onButtonPressed(Button.B, function () {
    if (numberselection) {
        numberselection = false
        radio.sendString("Select")
    }
    if (guessing) {
        guessing = false
        radio.sendNumber(guessA)
    }
    basic.clearScreen()
})
let guessA = 0
let numberA = 0
let guessing = false
let numberselection = false
numberselection = true
guessing = false
basic.forever(function () {
	
})
