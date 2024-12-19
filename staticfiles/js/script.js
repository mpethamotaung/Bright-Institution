// Navbar Toggle
const navbarToggler = document.querySelector(".navbar-toggler");
const navLinks = document.querySelector(".nav-links");
const navItems = navLinks.querySelectorAll("li a");
const backToTopButton = document.querySelector(".back-to-top");

navbarToggler.addEventListener("click", mobileMenu);

function mobileMenu() {
    navbarToggler.classList.toggle("active");
    navLinks.classList.toggle("active");
}

// Close Navbar Toggle Menu
navItems.forEach(link => link.addEventListener("click", function(e) {
    e.preventDefault(); // Prevent default anchor click behavior
    closeMenu(); // Close the mobile menu
    
    // Smooth scroll to the section
    const targetId = this.getAttribute("href").substring(1);
    const targetElement = document.getElementById(targetId);
    if (targetElement) {
        targetElement.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }
}));

function closeMenu() {
    navbarToggler.classList.remove("active");
    navLinks.classList.remove("active");
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
