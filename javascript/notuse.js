alert("I'm Working. I'm Js. I'm Beautiful. I'm worth it");

console.log(console)

function sayHello(name, age) {
  console.log('Hello!', name, " you have", age, " years of age.");
}

function sayHello(name, age) {
  console.log(`Hello ${name} you are ${age} years old`);
}

sayHello("Nicolas", 15);


function sayHello(name, age) {
  return `Hello ${name} you are ${age} years old`;
}

const greetNicolas = sayHello("Nicolas", 15)

console.log(greetNicolas)

const title = document.getElementById("title");

console.log(title)

title.innerHTML = "Hi! From JS";

const title = document.querySelector("#title");

title.innerHTML = "HI! From JS"
title.style.color = "red";
document.title = "I own you now";

function handleResize() {
  console.log("I have been resized");
}

function handleClick(event) {
  title.style.color = "blue";
}

title.addEventListener("click", handleClick);

window.addEventListener("resize", handleResize);

if (10 === 10) {
  console.log("hi");
}
else {
  console.log("ho");
}

const age = prompt("How old are you?");

if (age > 18) {
  console.log("you can drink");
} else {
  console.log("you can't");
}

const title = document.querySelector("#title");

const BASE_COLOR = "rgb(52, 73, 94)";
const OTHER_COLOR = "#7f8c8d";

function handleClick() {
  const currentColor = title.style.color;
  if (currentColor === BASE_COLOR) {
    title.style.color = OTHER_COLOR;
  } else {
    title.style.color = BASE_COLOR;
  }
}

function init() {
  title.style.color = BASE_COLOR;
}

title.addEventListener("click", handleClick);
init();

function handleOffline() {
  console.log("bye bye");
}

function handleOnline() {
  console.log("Welcome back");
}

window.addEventListener("offline", handleOffline);
window.addEventListener("online", handleOnline);
