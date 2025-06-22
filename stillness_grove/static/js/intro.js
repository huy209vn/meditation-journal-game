const Intro = {
    init() {
        const intro = document.getElementById('intro');
        const game = document.getElementById('game-container');
        const buttonRow = document.querySelector('.button-row');
        if (!intro || !game) return;

        intro.addEventListener('animationend', () => {
            intro.style.display = 'none';
            game.classList.add('show');
            if (buttonRow) {
                setTimeout(() => {
                    buttonRow.classList.add('show-buttons');
                }, 500);
            }
        });
    }
};

export default Intro;
