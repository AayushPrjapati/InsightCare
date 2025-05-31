// Function to toggle the dropdown menu
  function toggleMenu() {
    const dropdown = document.querySelector('.dropdown');
    // Toggle dropdown visibility
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
  }

  // Form submission handler
  document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Thank you for contacting us. We will get back to you shortly.');
    event.target.reset();
  });
