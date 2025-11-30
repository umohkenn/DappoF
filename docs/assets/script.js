const navbar = document.querySelector('.navbar');
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

if (navToggle) {
  navToggle.addEventListener('click', () => {
    navbar.classList.toggle('open');
  });
}

// Close navigation on link click (mobile)
if (navLinks) {
  navLinks.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navbar.classList.remove('open');
    });
  });
}

// Add subtle scroll reveal
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.16 }
);

document.querySelectorAll('.card, .feature-card, .stat, .tour-grid__item').forEach((el) => {
  el.classList.add('fade');
  observer.observe(el);
});
