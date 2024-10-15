let nav = document.getElementById('nav');
let bars = document.getElementById('bars');

bars.addEventListener("click" ,() => {
    if (nav.style.display === "block") {
        nav.style.display = "none";
    } else {
        nav.style.display = "block";
        nav.style.backgroundColor = "white";
    }
});
 
let body = document.getElementById('body');
let button = document.getElementById('mode-button');

button.addEventListener("click",() => {
    body.classList.toggle('dark-mode');
});