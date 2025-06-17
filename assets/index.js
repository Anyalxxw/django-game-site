const questions = document.querySelectorAll('.question');
const backgroundImage = document.getElementById('game-image');
const container = document.getElementById('all-platforms');


questions.forEach(question => {
    question.addEventListener('click', () => {
        const li = question.parentElement
        li.classList.toggle('active');
    });
});

function loadGame(gameID){
    fetch(`/api/game/${gameID}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('game-title').innerHTML = data.title;
            document.getElementById('game-description').innerHTML = data.description;
            document.getElementById('game-rating').innerHTML = data.rating;
            document.getElementById('game-release-date').innerHTML = data.release_date;
            document.getElementById('game-genre').innerHTML = data.genre.join(' - ');
            document.getElementById('few-platforms').innerHTML = data.platforms.join(' - ').slice(0,25);

            container.innerHTML = '';
            data.platforms.forEach(platform => {
                const p = document.createElement('p');
                p.textContent = platform
                container.appendChild(p)
            });

            backgroundImage.style.background = `
            linear-gradient(to right, rgba(28, 27, 41, 1), rgba(28, 27, 41, 0.6), rgba(0, 0, 0, 0)),
            url(${data.image_url})`;
            backgroundImage.style.backgroundSize = 'cover';
            backgroundImage.style.backgroundPosition = 'center center';
            backgroundImage.style.backgroundRepeat = 'no-repeat';
            backgroundImage.style.backgroundAttachment = 'fixed';
        })
}


























