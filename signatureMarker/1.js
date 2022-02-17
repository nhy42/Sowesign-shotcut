const canvas = document.getElementById("signBox");
const ctx = canvas.getContext("2d");
let coord = { x: 0, y: 0 };

var logs = [];


document.addEventListener("mousedown", start);
document.addEventListener("mouseup", stop);
window.addEventListener("resize", resize);

resize();

function resize() {
    ctx.canvas.width = 700;
    ctx.canvas.height = 370;
}

function reposition(event) {
    coord.x = event.clientX - canvas.offsetLeft;
    coord.y = event.clientY - canvas.offsetTop;
}

function start(event) {
    document.addEventListener("mousemove", draw);
    reposition(event);
}

function stop() {
    document.removeEventListener("mousemove", draw);
    if (logs[logs.length - 1] != 0) {
        logs.push(0);
    }
    resultInTextarea();
}

function resultInTextarea() {
    let text = "";
    for (var i = 0; i < logs.length; i++) {
        if (logs[i] != 0) {
            text += "" + logs[i][0] + "," + logs[i][1] + "\n";
        } else {
            text += "0\n";
        }
    }
    document.getElementById("resultArea").innerHTML = text;
}

function draw(event) {
    ctx.beginPath();
    ctx.lineWidth = 5;
    ctx.lineCap = "round";
    ctx.strokeStyle = "#FF0000";
    ctx.moveTo(coord.x, coord.y);
    reposition(event);
    if (coord.x <= 700 && coord.x >= 0 && coord.y <= 370 && coord.y >= 0) {
        logs.push([coord.x, coord.y]);
    }
    ctx.lineTo(coord.x, coord.y);
    ctx.stroke();
}