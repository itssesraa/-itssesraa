// Interactivity for the Moon Beauty page

// wait until DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  // toggle favorite hearts on product cards
  const favorites = document.querySelectorAll('.favorite');

  favorites.forEach(fav => {
    fav.addEventListener('click', () => {
      const icon = fav.querySelector('i');
      if (icon.classList.contains('bi-heart')) {
        icon.classList.remove('bi-heart');
        icon.classList.add('bi-heart-fill');
        icon.style.color = '#e63946';
      } else {
        icon.classList.remove('bi-heart-fill');
        icon.classList.add('bi-heart');
        icon.style.color = '#ccc';
      }
    });
  });

  // simple handler for the "Shop Now" button
  const shopBtn = document.querySelector('.hero .btn');
  if (shopBtn) {
    shopBtn.addEventListener('click', () => {
      window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    });
  }
});
