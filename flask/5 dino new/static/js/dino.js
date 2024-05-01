const dino = document.getElementById('dino')
const cactus = document.getElementById('cactus')

let scoreCounter = 0

function jump() {
	if (dino.classList != 'jump') {
		dino.classList.add('jump')

		setTimeout(function () {
			dino.classList.remove('jump')
		}, 300)
	}
}

document.addEventListener('keydown', function (event) {
	jump()
})

let isAlive = setInterval(function () {
	let dinoTop = parseInt(window.getComputedStyle(dino).getPropertyValue('top'))
	let cactusLeft = parseInt(
		window.getComputedStyle(cactus).getPropertyValue('left')
	)

	if (cactusLeft < 40 && cactusLeft > 0 && dinoTop >= 140) {
		alert('Game Over! Your score is: ' + Math.round(scoreCounter))
		scoreCounter = 0 // Reset the score
		document.getElementById('scoreValue').innerHTML = scoreCounter
	} else {
		scoreCounter += 0.01
		document.getElementById('scoreValue').innerHTML = Math.round(scoreCounter)
	}
}, 10)
