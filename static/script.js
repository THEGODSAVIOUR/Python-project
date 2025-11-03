// Adds fade-in animation to all elements when page loads
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.fade-in').forEach((el, i) => {
        el.style.animationDelay = `${i * 0.2}s`;
        el.classList.add('visible');
    });
});
