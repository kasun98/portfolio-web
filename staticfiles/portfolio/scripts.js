document.addEventListener('DOMContentLoaded', function() {
    
});

function toggleSkillDetails(id, element) {
    var detailsElement = document.getElementById(id);
    var arrowElement = element.querySelector('.arrow');
    if (detailsElement.classList.contains('show')) {
        detailsElement.classList.remove('show');
        arrowElement.classList.remove('rotate');
    } else {
        detailsElement.classList.add('show');
        arrowElement.classList.add('rotate');
    }
}
