let canvasWidth = 640, canvasHeight = 360, shapeWidth = 200, shapeHeight = 100;

let add = (x, y) => {return x + y;}
console.log(add(3, 4));

function setup() {
  createCanvas(canvasWidth, canvasHeight);
  console.log('setup');
}

function draw() {
  background(0);
  // ellipse(200, 200, 50, 50);
  rect(canvasWidth/2-shapeWidth/2, canvasHeight/2-shapeHeight/2, shapeWidth, shapeHeight);
  console.log('draw');
}