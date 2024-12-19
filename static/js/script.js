// Navbar Toggle
const navbarToggler = document.querySelector(".navbar-toggler");
const navLinksContainer = document.querySelector(".nav-links-container");
const backToTopButton = document.querySelector(".back-to-top");

navbarToggler.addEventListener("click", mobileMenu);

function mobileMenu() {
    navbarToggler.classList.toggle("active");
    navLinksContainer.classList.toggle("active");
}

// Show or hide the back-to-top button based on scroll position
window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
        backToTopButton.classList.add("visible");
    } else {
        backToTopButton.classList.remove("visible");
    }
});

// Scroll smoothly back to top when the button is clicked
backToTopButton.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});
