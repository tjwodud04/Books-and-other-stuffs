/*alert("I'm Working. I'm Js. I'm Beautiful. I'm worth it");*/

/*console.log(console)*/

/*function sayHello(name, age) {
  console.log('Hello!', name, " you have", age, " years of age.");
}*/

/*function sayHello(name, age) {
  console.log(`Hello ${name} you are ${age} years old`);
}

sayHello("Nicolas", 15);*/

/*
function sayHello(name, age) {
  return `Hello ${name} you are ${age} years old`;
}

const greetNicolas = sayHello("Nicolas", 15)

console.log(greetNicolas)
*/

/*
const title = document.getElementById("title");

console.log(title)

title.innerHTML = "Hi! From JS";
*/

const title = document.querySelector("#title");
/*
title.innerHTML = "HI! From JS"
title.style.color = "red";
document.title = "I own you now";
*/

function handleResize() {
  console.log("I have been resized");
}

function handleClick(event) {
  title.style.color = "blue";
}

title.addEventListener("click", handleClick);

window.addEventListener("resize", handleResize);