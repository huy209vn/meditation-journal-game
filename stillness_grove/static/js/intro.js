const Intro = {
    init() {
        const intro = document.getElementById('intro');
        const game = document.getElementById('game-container');
        if (!intro || !game) return;

        intro.addEventListener('animationend', () => {
            intro.style.display = 'none';
            game.classList.add('show');
        });
    }
};

export default Intro;
