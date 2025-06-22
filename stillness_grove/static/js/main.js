import BreathingOverlay from './breathingOverlay.js';
import Ripple from './ripple.js';
import Intro from './intro.js';

// Initialize modules when DOM is ready
window.addEventListener('DOMContentLoaded', () => {
    Intro.init();
    BreathingOverlay.init();
    Ripple.init();
});
