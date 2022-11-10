const setCheckboxes = () => {
  const checkboxes = document.querySelectorAll('.form-block.checkbox');
  if (!checkboxes) return;
  
  checkboxes.forEach(checkbox => {
    checkbox.onclick = function() {
      checkbox.classList.toggle('active');
    }
  });
}

const init = () => {
  setCheckboxes();
}

window.addEventListener('DOMContentLoaded', init);