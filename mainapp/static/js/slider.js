let index = 0;
const slides = document.querySelector(".slides");
const totalSlides = document.querySelectorAll(".slide").length;
let autoSlideInterval;
let resumeTimeout;
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

function updateSlide() {
  slides.style.transform = `translateX(-${index * 25}%)`;
}

function startAutoSlide() {
  autoSlideInterval = setInterval(() => {
    index = (index + 1) % totalSlides;
    updateSlide();
  }, 3000); // змінювати слайд кожні 3 секунди
}

function stopAutoSlide() {
  clearInterval(autoSlideInterval);
}

// Функція для зупинки автоперемикання та відновлення його через 5 секунд бездіяльності
function resetAutoSlide() {
  stopAutoSlide();
  clearTimeout(resumeTimeout);
  resumeTimeout = setTimeout(() => {
    startAutoSlide();
  }, 5000); // 5 секунд затримки перед відновленням автоперемикання
}

document.querySelector(".prev").addEventListener("click", () => {
  index = (index - 1 + totalSlides) % totalSlides;
  updateSlide();
  resetAutoSlide();
  updateNavigation()
});

document.querySelector(".next").addEventListener("click", () => {
  index = (index + 1) % totalSlides;
  updateSlide();
  resetAutoSlide();
  updateNavigation()
});

function updateNavigation() {
  if (index === 0) {
    prevButton.style.visibility = 'hidden';
  } else {
    prevButton.style.visibility = 'visible';
  }
  // Якщо останній слайд — приховуємо кнопку "next"
  if (index === totalSlides - 1) {
    nextButton.style.visibility = 'hidden';
  } else {
    nextButton.style.visibility = 'visible';
  }
}


// Запуск автоперемикання при завантаженні сторінки
startAutoSlide();