const title = document.querySelector("#title");

const CLICK_CLASS = "clicked";

function handleClick() {
  /*
  const hasClass = title.classList.contains(CLICKED_CLASS);
  if (hasClass) {
    title.classList.remove(CLICKED_CLASS;
  } else {
    title.classList.add(CLICKED_CLASS);
  }*/
  title.classList.toggle(CLICK_CLASS);
}

function init() {
  title.addEventListener("click", handleClick);
}

init();