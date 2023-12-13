
/* +++++++++ searching ++++++++++ */
document.addEventListener('keydown', (event) => {
  let search = document.getElementById("game-input");
  if (event.key === 'Enter') {
    window.location.href = `https://game-finder-one.vercel.app/${search.value}`
  }
})


/* +++++++++++ auto scroling ++++++++++++ */
document.addEventListener("DOMContentLoaded", function () {
  var moves = document.querySelectorAll(".games");
  var art = document.querySelectorAll(".games .art");
  setInterval(() => {
    // Scroll the container horizontally by a small amount (adjust as needed)
    moves.forEach(element => {
      element.scrollLeft += 1;
      if (element.scrollLeft >= element.offsetWidth * art.length / 10) {
        element.scrollLeft = 0;
      }
    });
  }, 50); // Adjust the interval as needed
});
