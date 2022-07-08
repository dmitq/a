const header = document.querySelector('.color_header');
const about = document.querySelector('.about');
header.addEventListener('mouseover', function() {
    about.classList.remove('hidden');
})
header.addEventListener('mouseout', function() {
    about.classList.add('hidden');
})
