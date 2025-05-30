// Main JavaScript file for Green Landscapes

document.addEventListener('DOMContentLoaded', function() {
    // Initialize before/after sliders if they exist
    const sliders = document.querySelectorAll('.before-after-slider');
    if (sliders.length > 0) {
        initBeforeAfterSliders();
    }

    // Initialize gallery filtering if it exists
    const galleryFilters = document.querySelector('.gallery-filters');
    if (galleryFilters) {
        initGalleryFilters();
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Booking form date validation - can't select dates in the past
    const bookingDateInputs = document.querySelectorAll('input[type="date"]');
    bookingDateInputs.forEach(input => {
        const today = new Date();
        const dd = String(today.getDate()).padStart(2, '0');
        const mm = String(today.getMonth() + 1).padStart(2, '0');
        const yyyy = today.getFullYear();
        const currentDate = yyyy + '-' + mm + '-' + dd;
        input.setAttribute('min', currentDate);
    });

    // Animate elements when they come into view
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    if (animatedElements.length > 0) {
        initScrollAnimations();
    }
});

// Before/After slider functionality
function initBeforeAfterSliders() {
    document.querySelectorAll('.before-after-slider').forEach(slider => {
        const handle = slider.querySelector('.slider-handle');
        const beforeDiv = slider.querySelector('.slider-before');
        
        let isDragging = false;
        
        // Mouse events
        handle.addEventListener('mousedown', () => {
            isDragging = true;
        });
        
        document.addEventListener('mouseup', () => {
            isDragging = false;
        });
        
        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            updateSliderPosition(e.clientX, slider, beforeDiv);
        });
        
        // Touch events for mobile
        handle.addEventListener('touchstart', () => {
            isDragging = true;
        });
        
        document.addEventListener('touchend', () => {
            isDragging = false;
        });
        
        document.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            updateSliderPosition(e.touches[0].clientX, slider, beforeDiv);
        });
    });
}

function updateSliderPosition(xPosition, slider, beforeDiv) {
    const sliderRect = slider.getBoundingClientRect();
    const newPos = (xPosition - sliderRect.left) / sliderRect.width;
    const boundedPos = Math.max(0, Math.min(1, newPos));
    
    beforeDiv.style.width = `${boundedPos * 100}%`;
    slider.querySelector('.slider-handle').style.left = `${boundedPos * 100}%`;
}

// Gallery filtering functionality
function initGalleryFilters() {
    const filterButtons = document.querySelectorAll('.gallery-filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            const filterValue = button.getAttribute('data-filter');
            
            // Filter gallery items
            galleryItems.forEach(item => {
                if (filterValue === 'all') {
                    item.style.display = 'block';
                } else if (item.getAttribute('data-category') === filterValue) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
}

// Scroll animation functionality
function initScrollAnimations() {
    const elements = document.querySelectorAll('.animate-on-scroll');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                // Stop observing once animation is applied
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    elements.forEach(element => {
        observer.observe(element);
    });
}

// Testimonial carousel (if needed)
function initTestimonialCarousel() {
    const testimonials = document.querySelector('.testimonials-container');
    if (!testimonials) return;
    
    const items = testimonials.querySelectorAll('.testimonial-item');
    const totalItems = items.length;
    let currentIndex = 0;
    
    // Navigation buttons
    const prevBtn = testimonials.querySelector('.testimonial-prev');
    const nextBtn = testimonials.querySelector('.testimonial-next');
    
    // Initialize first item as active
    items[0].classList.add('active');
    
    // Update which item is shown
    function showItem(index) {
        items.forEach(item => item.classList.remove('active'));
        items[index].classList.add('active');
    }
    
    // Event listeners for navigation
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + totalItems) % totalItems;
            showItem(currentIndex);
        });
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % totalItems;
            showItem(currentIndex);
        });
    }
    
    // Auto rotate if enabled
    const autoRotate = testimonials.getAttribute('data-auto-rotate') === 'true';
    if (autoRotate) {
        setInterval(() => {
            currentIndex = (currentIndex + 1) % totalItems;
            showItem(currentIndex);
        }, 5000);
    }
}
