input.onButtonPressed(Button.A, function () {
    if (nb < 10) {
        nb += 1
        basic.showNumber(nb)
    }
})
input.onButtonPressed(Button.B, function () {
    if (nb >= 10) {
    	
    } else {
        nb += 1
        basic.showNumber(nb)
    }
})
let nb = 0
nb = 1
basic.showNumber(nb)
basic.forever(function () {
	
})
