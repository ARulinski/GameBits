function toggleMenu() {
    const navbarLeft = document.querySelector('.navbar-left');
    const navbarRight = document.querySelector('.navbar-right');
    navbarLeft.style.display = navbarLeft.style.display === 'flex' ? 'none' : 'flex';
    navbarRight.style.display = navbarRight.style.display === 'flex' ? 'none' : 'flex';
}

function toggleDropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.matches('.avatar')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

 $(document).ready(function(){
            // JavaScript for glitch-like background animation
            function createGlitch() {
                var lines = 20; // Number of glitch lines
                var colors = ['#ff00ff', '#00ffff']; // Glitch colors
                var width = $(window).width();
                var height = $(window).height();
                for (var i = 0; i < lines; i++) {
                    var xPos = Math.random() * width;
                    var yPos = Math.random() * height;
                    var color = colors[Math.floor(Math.random() * colors.length)];
                    var glitchLine = $('<div></div>').css({
                        position: 'absolute',
                        top: yPos + 'px',
                        left: xPos + 'px',
                        width: '2px',
                        height: '100%',
                        background: color,
                        opacity: '0.8',
                        animation: 'glitchAnimation ' + (Math.random() * 2 + 1) + 's linear infinite'
                    });
                    $('.background-animation').append(glitchLine);
                }
            }

            // Call createGlitch function initially
            createGlitch();

            // Window resize event to adjust glitch lines on window resize
            $(window).resize(function() {
                $('.background-animation').empty(); // Clear previous lines
                createGlitch(); // Recreate glitch lines
            });
        });