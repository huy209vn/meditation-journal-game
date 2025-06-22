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

Subtle, User-Driven Unlockables

Unlockables fade in gently; no popups, no fireworks

New plants, pets, backgrounds arrive with slow, ambient animations

Naming, moving, or tending unlocks happens in-world, not via notification

Unlocks often appear after reflection, not just action

Integration With Work Platforms (Optional)

Completing tasks (e.g. jobs in FixNow) can unlock subtle new grove elements

Rewards reinforce restorative cycles, not grind

Journaling and meditation can also trigger world evolution

s

🔬 Scientific/Design Foundation

Entrainment: visual/audio rhythm syncing with player physiology

Box Breathing: scientifically backed breathing pattern for calming nervous system

Flow State Psychology: gentle challenge + high feedback = meditative focus

Biofeedback Potential: future add-on—connect microphone or device sensors

Low-Stimulation Reward System: Unlockables designed as whispers, not shouts (see chat for full UX principles)

🛠️ Tech Stack (Browser MVP & Full-Stack)

Frontend: HTML/CSS/JavaScript for canvas-based rendering and breathing overlay

Canvas API: for animated island and ripple effects

AudioContext/Web Audio API: for interactive ambient sounds

Backend (for journaling, unlockables, and user sync): Django + SQLite/PostgreSQL

Data Flow: All unlocks, journals, and garden state stored in SQL via Django ORM

AJAX/REST: Use Django REST Framework or AJAX for async feature unlocks and journal saves

Optional: Firebase or localStorage for extra persistence if offline

🎨 Aesthetic

Pastel tones, soft motion, hand-drawn style

Lo-fi Ghibli vibes

UI is minimal or hidden—nothing breaks immersion

Subtle animations, no overstimulation; everything blends

🧘️ Player Outcome

After a session, player feels:

Mentally clearer

More present

Emotionally balanced

Like they’ve played with peace, not escaped from stress

Grove feels more alive, not just "more stuff unlocked"

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

5. Gamification (Optional, All Subtle)

Streaks for journaling or meditating (no counters, just ambient changes)

Unlockable themes/visuals (fade in, never popup)

Badges for self-care milestones (gentle highlight, not alert)

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

Plant

id

name

image

unlock_condition

Pet

id

name

image

unlock_condition

UserProfile

id

user (OneToOne)

unlocked_plants (M2M)

pets (M2M)

garden_state (JSON)

✨ MVP & Immersive UX Scope Summary

*(This game is delivered as a single-page web app. All navigation happens through overlays and modals rather than loading new pages.)*

Feature

Must Have

Tech

One immersive URL

✅

Django + JS

Animated Fade-in Intro

✅

JS + CSS

Breathing Overlay

✅

JS + Canvas

Ripple Interaction

✅

JS + Canvas

Journal Entry + Presets

✅

Django + HTML/CSS/JS

Unlockables (Subtle)

✅

Django + JS/CSS

Ambient Music

⬜

Web Audio API

Environmental FX

⬜

JS Events + Canvas

World Evolution

⬜

SQL/JSON/Django

Meditation Mode

✅

JS + Django Integration

## Development Setup

To run the project locally using Django:

1. Create and activate a virtual environment.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install the required Python packages.
   ```bash
   pip install -r requirements.txt
   ```
3. Apply database migrations.
   ```bash
   cd stillness_grove
   python manage.py migrate
   ```
4. Start the development server.
   ```bash
   python manage.py runserver
   ```
   Then open `http://localhost:8000/` in your browser.
