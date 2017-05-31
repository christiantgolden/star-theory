var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

var rightPressed = false;
var leftPressed = false;

//hero stuff
var heroWidth = 32;
var heroHeight = 32;
var heroX = (canvas.width-heroWidth)/2;
var heroY = canvas.height-heroHeight;
var Hero = new Image();
Hero.src = "Shoot_Them.bmp";
//my stuff
var enemyWidth = 16;
var enemyHeight = 16;
var enemyXList = [];
var enemyYList = [];
var enemyX = 0;
var enemyY = 0;

//laserCoords
var laserWidth = 4;
var laserHeight = canvas.height;
var laserX = heroX + (heroWidth/2) - 2;
var laserY = canvas.height;
//my added inputs
var spacePressed = false;
var downPressed = false;

var hitFlag = 0;
var score = 0;

document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

//add enemy x's and enemy y's to arrays/lists to be 
//referenced in drawEnemyShips
//add to this list every cycle with a function 
//that is called each cycle to generate a random x and y
//to be appended to the list of enemy x's and y's

function genEnemyXY(){
	if (Math.floor(Math.random() * 5) == 1){
		enemyX = Math.floor(Math.random()*canvas.width + 1);
		enemyY = Math.floor(Math.random()* -canvas.height);
		if (spacePressed == false || laserX < enemyXList[i] || laserX > enemyXList[i] + enemyWidth){
			enemyXList[enemyXList.length] = enemyX;
			enemyYList[enemyYList.length] = enemyY;
		}
	}
}

function drawEnemyShips(){
	for (i = 0; i <= enemyYList.length; i++){//https://stackoverflow.com/questions/5597060/detecting-arrow-key-presses-in-javascript
		if (spacePressed == false || laserX < enemyXList[i] || laserX > enemyXList[i] + enemyWidth){
			ctx.beginPath();
			ctx.rect(enemyXList[i], enemyYList[i], enemyWidth, enemyHeight);
			ctx.fillStyle = ("#fff");
			ctx.fill();
			ctx.closePath();
		}
		/*below is test script
		else if (spacePressed && laserX >= enemyXList[i] && laserX <= enemyXList[i] + enemyWidth){
			if (i < enemyXList.length){
				i++;
			}
		} //this is where test script ends... delete if blocks still blinking...*/
	}
}

/*function shipCollide(){
	for (i = 0; i < enemyXList.length; i++){
		if(spacePressed && enemyXList[i] == laserX){
			hitFlag = 1;
		}
		else{
			hitFlag = 0;
		}
	}
}*/

function keyDownHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = true;
    }
    else if(e.keyCode == 37) {
        leftPressed = true;
    }
    else if(e.keyCode == 32) {
    	spacePressed = true;
    }
    else if(e.keyCode == 40){
    	downPressed = true;
    }
}
function keyUpHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = false;
    }
    else if(e.keyCode == 37) {
        leftPressed = false;
    }
    else if(e.keyCode == 32) {
    	spacePressed = false;
    }
    else if(e.keyCode == 40){
    	downPressed = false;
    }
}

function drawHero(){
	ctx.drawImage(Hero, heroX, heroY);
}

//my added drawLaser function
function drawLaser(){
	ctx.beginPath();
	ctx.rect(laserX, canvas.height - laserHeight, laserWidth, laserHeight);
	ctx.fillStyle = 'rgb(' + 
		Math.floor(Math.random() * 255) + ',' +
		Math.floor(Math.random() * 255) + ',' +
		Math.floor(Math.random() * 255) + ')';
	ctx.fill();
	ctx.closePath();
}

function drawStarfield(){
	var starField = [];
	var randColor = Math.floor(Math.random() * 255);
	for (i = 0; i < Math.floor(Math.random() * 100); i++){
		var randX = Math.floor(Math.random() * canvas.width);
		var randY = Math.floor(Math.random() * canvas.height);
		var starSize = Math.floor(Math.random() * 4);
		ctx.beginPath();
		ctx.rect(randX, randY, starSize, starSize);
		ctx.fillStyle = 'rgb(' + 
			Math.floor(Math.random() * 255) + ',' +
			Math.floor(Math.random() * 255) + ',' +
			Math.floor(Math.random() * 255) + ')';
		ctx.fill();
		ctx.closePath(); 
	}
}

function drawScore(){
	ctx.font = "16px Arial";
	ctx.fillStyle = "#fff";
	ctx.fillText("Score: " +score, 8, 20);
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawStarfield();
    if(spacePressed){
    	drawLaser();
    }
    drawHero();
    genEnemyXY();
    drawEnemyShips();

    for(i = 0; i < enemyYList.length; i++){
    	if (spacePressed == false || laserX < enemyXList[i] || laserX > enemyXList[i] + enemyWidth){
    		enemyYList[i] += 1;
    	}
    	else if(spacePressed && laserX >= enemyXList[i] && laserX <= enemyXList[i] + enemyWidth && enemyYList[i] >= 0){
    		enemyYList[i] -= canvas.height * Math.floor(Math.random() * canvas.height);
    		score++;
    	}
    }

    if(rightPressed && heroX < canvas.width) {
        laserX += 5;
        heroX += 5;
    }
    else if(rightPressed && heroX >= canvas.width){
    	laserX -= canvas.width + heroWidth;
    	heroX -= canvas.width + heroWidth;
    }
    else if(leftPressed && heroX > 0 - heroWidth) {
        laserX -= 5;
        heroX -= 5;
    }
    else if(leftPressed && heroX <= 0 - heroWidth){
    	laserX += canvas.width + heroWidth;
    	heroX += canvas.width + heroWidth;
    }

    drawScore();

    requestAnimationFrame(draw);
}

draw();