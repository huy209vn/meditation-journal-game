🌿 Stillness Grove – Game Design Document

🌟 Core Concept

A relaxing, therapeutic game where players gently shape a living floating island through rhythm, breath, and minimal interactions. The goal is not to win, but to enter a state of calm focus and flow.

🧠 Core Principles

Low cognitive load: no timers, combos, or high-speed input

Simple interactions: drag, click, float, breathe

Rhythmic feedback: visuals, music, and breathing in sync

Beautiful repetition: actions loop and evolve, not escalate

Micro-control: small nudges give satisfying, aesthetic reactions

Therapeutic UX: feels like meditating with your hands

🌿 Game Features

Floating Island World

Soft, painterly 2D or 2.5D landscape with trees, rivers, clouds, fog

Breathing Overlay (Box Breathing Pulse)

A semi-transparent visual overlay that subtly pulses to guide 4-4-4-4 breathing

Ripple Interactions

Click or tap to send out ripples in water or air—responsive but calming

Environmental Tuning

Drag clouds → they merge and rain

Tap trees → play soft notes

Shape wind, adjust light, grow plants

Dynamic Ambient Music

Music builds as you interact

Loops evolve, matching mood and actions

Could sync with breath mic input if enabled

Slow Evolution

Every login slightly changes the world

More birds, flowers, colors—but always subtle

Sound Garden / Glow Pond Minigames

Optional micro-zones with simple, musical or visual play

Drop stones into a glowing pond and watch fish swim to the rhythm

🔬 Scientific/Design Foundation

Entrainment: visual/audio rhythm syncing with player physiology

Box Breathing: scientifically backed breathing pattern for calming nervous system

Flow State Psychology: gentle challenge + high feedback = meditative focus

Biofeedback Potential: future add-on—connect microphone or device sensors

🛠️ Tech Stack (Browser MVP)

Frontend: HTML/CSS/JavaScript for canvas-based rendering and breathing overlay

Canvas API: for animated island and ripple effects

AudioContext/Web Audio API: for interactive ambient sounds

Backend (for journaling): Django + SQLite

Optional: Firebase or localStorage to save session state and slow world evolution

🎨 Aesthetic

Pastel tones, soft motion, hand-drawn style

Lo-fi Ghibli vibes

UI is minimal or hidden—nothing breaks immersion

🧘️ Player Outcome

After a session, player feels:

Mentally clearer

More present

Emotionally balanced

Like they’ve played with peace, not escaped from stress

📓 Journal System Integration

1. Beautiful Journal UI

Pastel, calming background (custom static image, frosted-glass card containers)

Responsive two-column layout:

Left: List of past entries (preset name, mood, timestamp, answers)

Right:

List of user-created “journal presets”

Form to create new preset (define prompts/questions)

Journal entry form dynamically rendered from selected preset

2. Custom Journal Presets

Users can create/edit/delete their own templates

Each preset has a title + list of questions

When writing, users select a preset → form updates accordingly

3. Dynamic Entry Creation

Journal entry records:

Preset used

Answers (JSON)

Mood (optional)

Timestamp

4. Meditation Feature

Standalone breathing mode with background animation

Visual + textual cues: "Inhale... Hold... Exhale... Hold..."

Affirmation on finish

Optional journaling afterward

5. Gamification (Optional)

Streaks for journaling or meditating

Unlockable themes/visuals

Badges for self-care milestones

📊 Database Structure

User (standard Django User model)

JournalPreset

id

user_id (FK)

title

questions (as JSON)

JournalEntry

id

user_id (FK)

preset_id (FK)

answers (as JSON)

mood

timestamp
