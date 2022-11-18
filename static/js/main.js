document.addEventListener("click", (e) => {
  const selector = '.form-block.checkbox';
  const closest = e.target.closest(selector);

  document.querySelectorAll(selector).forEach(element => element.classList.remove('active'));

  if (closest) closest.classList.add('active');
});

window.addEventListener('DOMContentLoaded', init);