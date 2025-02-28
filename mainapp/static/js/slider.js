function initializeSlider(sliderId) {
  let index = 1; // Починаємо з 1, оскільки перший слайд - це копія останнього
  const slider = document.querySelector(`#${sliderId}`);
  const slides = slider.querySelector(".slides");
  const slide = slider.querySelectorAll(".slide");
  const totalSlides = slide.length;
  const prevButton = slider.querySelector('.prev');
  const nextButton = slider.querySelector('.next');
  let autoSlideInterval;
  let resumeTimeout;

  // Встановлюємо початкову позицію
  slides.style.transform = `translateX(-${index * 100}%)`;

  function updateSlide() {
    slides.style.transition = 'transform 0.5s ease-in-out';
    slides.style.transform = `translateX(-${index * 100}%)`;
  }

  function startAutoSlide() {
    autoSlideInterval = setInterval(() => {
      index++;
      updateSlide();
      handleSeamlessTransition();
    }, 3000);
  }

  function stopAutoSlide() {
    clearInterval(autoSlideInterval);
  }

  function resetAutoSlide() {
    stopAutoSlide();
    clearTimeout(resumeTimeout);
    resumeTimeout = setTimeout(() => {
      startAutoSlide();
    }, 5000);
  }

  function handleSeamlessTransition() {
    if (index >= totalSlides - 1) {
      setTimeout(() => {
        slides.style.transition = 'none';
        index = 1;
        slides.style.transform = `translateX(-${index * 100}%)`;
      }, 500);
    } else if (index <= 0) {
      setTimeout(() => {
        slides.style.transition = 'none';
        index = totalSlides - 2;
        slides.style.transform = `translateX(-${index * 100}%)`;
      }, 500);
    }
  }

  prevButton.addEventListener("click", () => {
    index--;
    updateSlide();
    handleSeamlessTransition();
    resetAutoSlide();
  });

  nextButton.addEventListener("click", () => {
    index++;
    updateSlide();
    handleSeamlessTransition();
    resetAutoSlide();
  });

  startAutoSlide();
}

document.addEventListener('DOMContentLoaded', () => {
  initializeSlider('slider1');
  initializeSlider('slider2');
});

