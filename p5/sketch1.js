var FileNumber;
var TweetNumber;
var currFont;
let ctx;
var img, imgURL;
let i = 0;
let q;
let s =
  " It was the bes as;lkdfa a asdfn,m t of times, i  asdf asdf  asdf a asdf adf  asdfa fadsf asdf a asdfa faf adsf aasf sd asdlfkm working    ";

async function fetchBackgroundImage() {
  //response = await fetch(`https://source.unsplash.com/random`);
  response = await fetch(`https://picsum.photos/1080/1080?random=2`);
  imgURL = response.url;
  print(imgURL);
  img = loadImage(imgURL, waitForElement);
}

////////////PRELOAD
function preload() {
  (async () => {
    response = await fetch("../middle.json");
    data = await response.json();
    console.log(data);
    FileNumber = parseInt(data["FileNumber"]);
    TweetNumber = parseInt(data["TweetNumber"]);

    currFont = loadFont("font.ttf");
    q = loadJSON(`../1/${FileNumber}.JSON`);
    console.log("hello");
  })();

  //fetchBackgroundImage();
}

////////////////////SETUP;

function setup() {
  frameRate(50);
  hello();
  // noLoop();
}
//hello

function hello() {
  textFont(currFont);

  let renderer = createCanvas(1080, 1080);
  img = loadImage(imgURL, waitForElement);
  ctx = renderer.drawingContext;
  //noLoop();
}

//////////////////DRAW
var a = 0;
var b = 0;
async function draw() {
  //image
  //frameCount(0.5);
  if (a == 0) {
    //await fetchBackgroundImage();
    fetchBackgroundImage();

    a = 1;
  }

  image(img, 0, 0);

  //rectangle

  fill(0, 0, 0, 100);
  rect(
    width / 10,
    height / 8,
    width - width / 5,
    height - height / 4,
    0,
    80,
    80,
    80
  );

  //Opening quotes
  fill(255);
  textSize(200);
  text("“", width / 10, height / 4);

  //CLosing quotes
  fill(255);
  textSize(200);
  text("”", width - width / 10, height - height / 10);

  //Author rectangle
  fill(0, 0, 0, 100);
  rect(
    width / 3,
    height / 1.11,
    width - width / 2,
    height - height / 1.09,
    80,
    80,
    80,
    80
  );
  //Author Name
  fill(255);
  textSize(50);
  text(
    `~${q[TweetNumber].author}`,
    width / 3,
    height / 1.1,
    width - width / 2,
    height - height / 1.09
  );

  //QUOTE SIZE
  fill(255);
  textSize(90);
  //console.log(s.length);
  if (s.length > 75 && s.length < 300) {
    textSize(90 - s.length / 6);
    //console.log("worked")
  }
  if (s.length > 300) {
    textSize(90 - s.length / 7);
  }

  //console.log(s.length)

  //QUOTE
  text(
    q[TweetNumber].text,
    width / 6,
    height / 5,
    width - width / 4,
    height - height / 3
  );
  console.log(q[i].text);
  console.log("working");

  canvass = `${FileNumber}#${TweetNumber}`;
  console.log("starting saving");
  if (b == 0) {
    setTimeout(() => {
      console.log("saving...");
      saveCanvas(canvass, "jpg");
      console.log("saved");
    }, 5000);
    b = 1;
  }

  console.log("next try");

  //saveit();
}

// //Save function
// function saveit() {
//   noLoop;
//   if (i < 1000) {
//     let canvass = "";
//     canvass = `${i}`;
//     saveCanvas(canvass, "jpg");
//     fetchBackgroundImage();
//     console.log(`downloaded pic ${canvass}`);
//     i++;
//     //console.log("worked");
//   }
// }

//Wait for elelment

function waitForElement() {
  {
    img.resize(width, height);
  }
  image(img, 0, 0);
}
