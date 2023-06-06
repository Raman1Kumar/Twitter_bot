var FileNumber;
var TweetNumber;
var currFont;
let ctx;
var img, imgURL;
let i = 0;
let q;
let s =
  " aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa    ";

//get background image and load
async function fetchBackgroundImage() {
  //response = await fetch(`https://source.unsplash.com/random`);
  response = await fetch(`https://picsum.photos/1080/1080?random=2`);
  imgURL = response.url;
  print(imgURL);
  img = await loadImage(imgURL, waitForElement);
}
//get background image and load end;


////////////PRELOAD
function preload() {
  (async () => {
    response = await fetch("../state_track/middle.json");
    data = await response.json();

    console.log(data);
    FileNumber = parseInt(data["FileNumber"]);
    TweetNumber = parseInt(data["TweetNumber"]);

    currFont = loadFont("./font/font.ttf");
    q = loadJSON(`../1/${FileNumber}.JSON`);
    
  })();

  //fetchBackgroundImage();
}


//SETUP;
function setup() {
  frameRate(1);
  hello();
  
}
//Setup end


//hello ->Responsible for adding background image(from: stackoverflow )
async function hello() {
  textFont(currFont);

  let renderer = createCanvas(1080, 1080);
  img = await loadImage(imgURL, waitForElement);
  ctx = renderer.drawingContext;
  //noLoop();
}
//hello end

//////////////////DRAW
var a = 0;
var b = 0;
async function draw() {
  

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
  //rectangle end;

  //Opening quotes
  fill(255);
  textSize(200);
  text("“", width / 10, height / 4);
  //Opening quotes end;


  //CLosing quotes
  fill(255);
  textSize(200);
  text("”", width - width / 10, height - height / 10);
  //Closing quotes end;


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
  //Author rectangle endl;


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
  //Author Name end


  //QUOTE SIZE
  fill(255);
  textSize(90);
  
  if (s.length > 75 && s.length < 300) {
    textSize(90 - s.length / 6);
  }
  if (s.length > 300) {
    textSize(90 - s.length / 7);
  }
  //QUOTE SIZE END

  

  //QUOTE
  text(
    q[TweetNumber].text,
    width / 6,
    height / 5,
    width - width / 4,
    height - height / 3
  );
  console.log(q[i].text);
  //Quote end


  // Save poster
  canvass = `${FileNumber}#${TweetNumber}`;
  console.log("starting saving");
  if (b == 0) {
    b = 1;
    await fetchBackgroundImage();

    setTimeout(async () => {
      await saveCanvas(canvass, "jpg");
    }, 6000);

  }

  console.log("next try");
  //Save poster end;

 
}
//Draw End;



//Wait for elelment
function waitForElement() {
  {
    img.resize(width, height);
  }
  image(img, 0, 0);
}
//Wait for element end
