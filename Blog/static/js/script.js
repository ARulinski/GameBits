function myFunction() {
    alert("Hello from a static file!");
  }                  
  function changeColor(element) {
    // Remove active class from all elements
    document.querySelectorAll('.bloc-icon').forEach(icon => {
        icon.classList.remove('active');
    });

    // Add active class to the clicked element
    element.classList.add('active');
}