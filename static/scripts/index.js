
const menuToggle = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');
menuToggle.addEventListener('click', () => {
  mobileMenu.classList.toggle('hidden');
  });
  
    let count = 1;

    function increaseCount() {
      count++;
      updateCountDisplay();
    }
  
    function decreaseCount() {
      if (count > 1) {
        count--;
        updateCountDisplay();
      }
    }
      function updateCountDisplay() {
      document.getElementById('countDisplay').textContent = `${count} تعداد`;
    }

