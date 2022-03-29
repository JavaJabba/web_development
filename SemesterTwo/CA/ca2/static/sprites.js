let canvas;
let context;

let fpsInterval = 1000/30
let now;
let then = Date.now();
let xhttp;


let player = {
    x : 0,
    y : 0,
    width : 32,
    height : 48,
    frameX : 0,
    frameY : 0,
    xChange : 0,
    yChange : 0,
}

let score = 0
let playerImage = new Image()
let moveLeft = false;
let moveRight = false;
let moveUp = false;
let moveDown = false;

IMAGES = {player: "static/player.png"}

document.addEventListener("DOMContentLoaded", init, false);

function init(){
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    floor = canvas.height - 27;
    player.x = canvas.width / 2;
    player.y = canvas.height / 2;
    playerImage.src = "static/player.png";

    window.addEventListener("keydown", activate, false);
    window.addEventListener("keyup", deactivate, false);

    draw();
}

function draw() {
    window.requestAnimationFrame(draw);
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval);

    //draw background
    context.clearRect(0,0, canvas.width, canvas.height);
    context.fillStyle = "#7cfc00";
    context.fillRect(0, 0, canvas.width, canvas.height);

    //draw player
    context.drawImage(playerImage, frameX * player.width, frameY * player.height, player.width, player.height, player.x, player.y, player.width, player.height);
    if ((moveLeft || moveRight) && (moveLeft && moveRight)) {
        player.frameX = (player.frameX + 1) % 8;
    }

    if (moveLeft) {
        player.xChange = player.xChange - 2;
        player.frameY = 9;
    }
    if (moveRight) {
        player.xChange = player.xChange + 2;
        player.frameY = 1;
    }
    if (moveUp) {
        player.yChange = player.yChange + 2;
    }
    if (moveDown) {
        player.yChange = player.yChange - 2;
    }

    //update player
    player.x = player.x + player.xChange
    player.y = player.y + player.yChange

    //Physics

    // Score
    score = score + 1
}

function activate(event){
    let key = event.key;
    if (key === "a"){
        moveLeft = true;
    } else if (key === "w") {
        moveUp = true;
    } else if (key === "d") {
        moveRight = true;
    } else if (key === "s") {
        moveDown = true;
    }
}

function deactivate(event){
    let key = event.key;
    if (key === "a"){
        moveLeft = false;
    } else if (key === "w") {
        moveUp = false;
    } else if (key === "d") {
        moveRight = false;
    } else if (key === "s") {
        moveDown = false;
    }
}

function stop(outcome) {
    window.cancelAnimationFrame(request_id);
    window.removeEventListener("keydown", activate);
    window.removeEventListener("keyup", deactivate);
    let outcome_element = document.querySelector("#outcome");
    outcome_element.innerHTML = outcome;

    let data = new FormData();
    data.append("score", score);

    xhttp = new XMLHttpRequest();
    xhttp.addEventListener("readystatechange", handle_response, false);
    xhttp.open("POST", "/store_score", true);
    xhttp.send(data);
}