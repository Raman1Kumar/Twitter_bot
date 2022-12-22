// fetch("https://type.fit/api/quotes")
//   .then(function(response) {
//     return response.json();
//   })
//   .then(function(data) {
//     console.log(data);
//   });
// import data from "./2.json" assert { type: "JSON" };
// console.log(data);

(async () => {
  response = await fetch("../middle.JSON");
  data = await response.json();
  console.log(data);
})();
