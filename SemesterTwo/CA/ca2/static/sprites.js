let canvas;
let context;
let request_id;

let fpsInterval = 1000 / 30;
let now;
let then = Date.now();
let xhttp;

let backgroundImage = new Image();
let background = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
];

let tilesPerRow = 8;
let tileSize = 32;

let player = {
    x: 0,
    y: 0,
    size: 34,
    frameX: 0,
    frameY: 0,
    xChange: 0,
    yChange: 0,
    facing: "none"
};

let enemySpawn = 0;
let enemy = [];
let score = 0;
let playerImage = new Image();
let enemyImage = new Image();
let moveLeft = false;
let moveRight = false;
let moveUp = false;
let moveDown = false;
let attack = false;

let IMAGES = { player: "static/player.png", background: "static/tileset.png", enemy: "static/enemy1.png" };

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    player.x = canvas.width / 2;
    player.y = canvas.height / 2;
    playerImage.src = "static/player.png";
    backgroundImage.src = "static/tileset.png";
    enemyImage.src = "static/enemy1.png";

    window.addEventListener("keydown", activate, false);
    window.addEventListener("keyup", deactivate, false);

    load_images(draw);
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
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "#7cfc00";
    context.fillRect(0, 0, canvas.width, canvas.height);
    for (let r = 0; r < 20; r += 1) {
        for (let c = 0; c < 32; c += 1) {
            let tile = background[r][c];
            if (tile >= 0) {
                let tileRow = Math.floor(tile / tilesPerRow);
                let tileCol = Math.floor(tile % tilesPerRow);
                context.drawImage(IMAGES.background, tileCol * tileSize, tileRow * tileSize, tileSize, tileSize, c * tileSize, r * tileSize, tileSize, tileSize);
            }
        }
    }


    if (moveLeft) {
        player.xChange = player.xChange - 1;
        player.frameY = 9;
        player.frameX = (player.frameX + 1) % 8;
        player.facing = "left";
    }
    if (moveRight) {
        player.xChange = player.xChange + 1;
        player.frameY = 1;
        player.facing = "right";
        player.frameX = (player.frameX + 1) % 8;
    }
    if (moveUp) {
        player.yChange = player.yChange - 1;
        player.facing = "up";
    }
    if (moveDown) {
        player.yChange = player.yChange + 1;
        player.facing = "down";
    }
    /* Attack attempt
    if (attack && facing === "left") {
        attack = true;
        player.frameY = 11;
        player.frameX = (player.frameX + 1) % 6
    }
    if (attack && facing === "right") {
        attack = true;
        player.frameY = 2;
        player.frameX = (player.frameX + 1) % 6
    }*/


    /*Scrap animation work
    if ((moveUp || moveDown) && player.facing === "left") {
        player.frameY = 9;
        player.frameX = (player.frameX + 1) % 8;
    } else if ((moveUp || moveDown) && player.facing === "right") {
        player.frameY = 1;
        player.frameX = (player.frameX + 1) % 8;
    }*/

    //update player
    player.x = player.x + player.xChange;
    player.y = player.y + player.yChange;

    //Physics
    player.yChange = player.yChange * 0.9;
    player.xChange = player.xChange * 0.9;

    // Going off screen
    if (player.x + player.size < 0) {
        player.x = canvas.width;
    } else if (player.x > canvas.width) {
        player.x = -player.size;
    } else if (player.y + player.size < 0) {
        player.y = canvas.height;
    } else if (player.y > canvas.height) {
        player.y = -player.size;
    }

    //enemy
    if (enemy.length < 5) {
        let e = {
            x: 0,
            y: randint(0, canvas.height),
            height: 32,
            width: 32,
            size: 10,
            xChange: 1.5,
            yChange: 1.5,
        };
        enemy.push(e);
        
    }
    //spawn enemy
    for (let e of enemy) {
        context.drawImage(IMAGES.enemy, e.x, e.y);
    }

    //draw player
    context.drawImage(IMAGES.player, player.frameX * 38, player.frameY * 32, 38, 32, player.x, player.y, 38, 32);

    for (let e of enemy) {
        //enemies going off screen
        if (e.x + e.size < 0) {
            e.x = canvas.width;
        } else if (e.x > canvas.width) {
            e.x = -e.size;
        } else if (e.y + e.size < 0) {
            e.y = canvas.height;
        } else if (e.y > canvas.height) {
            e.y = -e.size;
        }
    }
    
    //move towards player depending on location
    for (let e of enemy){
        if (e.x < player.x) {
            e.x = e.x + e.xChange;
        } else if (e.x > player.x) {
            e.x = e.x - e.xChange;
        } else if (e.x === player.x && e.y < player.y){
            e.y = e.y + e.yChange;
        } else if (e.x === player.x && e.y > player.y){
            e.y = e.y - e.yChange;
        }

        if (e.y < player.y) {
            e.y = e.y + e.yChange;
        } else if (e.y > player.y) {
            e.y = e.y - e.yChange;
        } else if (e.y === player.y && e.x < player.x){
            e.x = e.x + e.xChange;
        } else if (e.y === player.y && e.x > player.x){
            e.x = e.x - e.xChange;
        }
    }

    //if player collides with enemy 
    for (let e of enemy) {
        if (player_collides(e)) {
            stop();
            return;
        }
    }

    // attempt at making enemies move away from each other to avoid overlap
    // for (let e of enemy) {
    //     if (enemy_collides(enemy, e)) {
    //         enemy.y = enemy.y + 1;
    //         e.y = e.y - 1;
    //     }
    // }

    // Score
    score = score + 1;
}

function activate(event) {
    let key = event.key;
    if (key === "a") {
        moveLeft = true;
    } else if (key === "w") {
        moveUp = true;
    } else if (key === "d") {
        moveRight = true;
    } else if (key === "s") {
        moveDown = true;
    }

    if (key === "e"){
        attack = true;
    }
}

function deactivate(event) {
    let key = event.key;
    if (key === "a") {
        moveLeft = false;
    } else if (key === "w") {
        moveUp = false;
    } else if (key === "d") {
        moveRight = false;
    } else if (key === "s") {
        moveDown = false;
    }

    if (key === "e"){
        attack = false;
    }
}


function player_collides(e) {
    if (player.x + player.size < e.x ||
        e.x + e.size < player.x ||
        player.y > e.y + e.size ||
        e.y > player.y + player.size) {
        return false;
    } else {
        return true;
    }
}

function enemy_collides(enemy, e) {
    if (enemy.x + enemy.size < e.x ||
        e.x + e.size < enemy.x ||
        enemy.y > e.y + e.size ||
        e.y > enemy.y + enemy.size) {
        return false;
    } else {
        return true;
    }
}

//attempt at player attacks.
// function player_attack(e){
//     if (attack) {
//         for (let e of enemy){
//             if (e.x === player.x + player.size ||
//                 e.x === player.x - player.size){
//                 enemy.delete(e)
//             }
//         }   
//     }
// }


function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
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

// function handle_response() {
//     if (xhttp.readyState === 4) {
//         if (xhttp.status === 200) {
//             if (xhttp.responseText === "success") {

//             } else {

//             }
//         }
//     }
// }

function load_images(callback) {
    let num_images = Object.keys(IMAGES).length;
    let loaded = function () {
        num_images = num_images - 1;
        if (num_images === 0) {
            callback();
        }
    };
    for (let name of Object.keys(IMAGES)) {
        let img = new Image();
        img.addEventListener("load", loaded, false);
        img.src = IMAGES[name];
        IMAGES[name] = img;
    }
}