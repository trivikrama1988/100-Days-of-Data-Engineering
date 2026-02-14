const fs = require('fs');
const path = require('path');

// Read exercises.md
const exercisesContent = fs.readFileSync('../exercises.md', 'utf8');
const days = [];

// Parse exercises.md to extract day information
const lines = exercisesContent.split('\n');
let currentPhase = '';
let currentDay = {};

for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();

    // Detect phase headers
    if (line.startsWith('### 🟢 Phase 1:')) {
        currentPhase = 'phase-1';
    } else if (line.startsWith('### 🔵 Phase 2:')) {
        currentPhase = 'phase-2';
    } else if (line.startsWith('### 🟠 Phase 3:')) {
        currentPhase = 'phase-3';
    } else if (line.startsWith('### 🟣 Phase 4:')) {
        currentPhase = 'phase-4';
    } else if (line.startsWith('### ⚫ Phase 5:')) {
        currentPhase = 'phase-5';
    }

    // Parse day rows (| **1** | Linux Kernel | **The Inode Explosion:** ... |)
    if (line.startsWith('| **') && line.includes('** |')) {
        const match = line.match(/\*\*(\d+)\*\*\s*\|\s*([^|]+)\s*\|\s*\*\*([^*]+)\*\*\s*(.*?)\s*\|/);
        if (match) {
            const dayNumber = parseInt(match[1]);
            const topic = match[2].trim();
            const exerciseTitle = match[3].trim();
            const exerciseDesc = match[4].trim();

            days.push({
                day: dayNumber,
                phase: currentPhase,
                topic: topic,
                exercise: `${exerciseTitle}: ${exerciseDesc}`,
                phaseName: getPhaseName(currentPhase),
                color: getPhaseColor(currentPhase)
            });
        }
    }
}

function getPhaseName(phase) {
    const phases = {
        'phase-1': 'The Metal',
        'phase-2': 'Distributed Foundation',
        'phase-3': 'Spark Mastery',
        'phase-4': 'Multi-Cloud',
        'phase-5': 'Production'
    };
    return phases[phase] || phase;
}

function getPhaseColor(phase) {
    const colors = {
        'phase-1': '#10b981',
        'phase-2': '#3b82f6',
        'phase-3': '#f59e0b',
        'phase-4': '#8b5cf6',
        'phase-5': '#1f2937'
    };
    return colors[phase] || '#64748b';
}

// Generate HTML for each day
days.forEach(day => {
    const html = generateDayHTML(day);
    const fileName = `day-${day.day.toString().padStart(2, '0')}.html`;
    const filePath = path.join(__dirname, '..', 'days', fileName);

    // Ensure directory exists
    const dir = path.dirname(filePath);
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }

    fs.writeFileSync(filePath, html);
    console.log(`Generated: ${fileName}`);
});

// Generate days index page
const daysIndexHTML = generateDaysIndexHTML(days);
fs.writeFileSync(path.join(__dirname, '..', 'days', 'index.html'), daysIndexHTML);

console.log(`Generated ${days.length} day pages`);

function generateDayHTML(day) {
    const prevDay = day.day > 1 ? day.day - 1 : null;
    const nextDay = day.day < 100 ? day.day + 1 : null;

    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day ${day.day}: ${day.topic} - 100 Days of Data Engineering</title>
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .phase-banner {
            background: ${day.color};
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            font-weight: 600;
            display: inline-block;
            margin-bottom: 1rem;
        }

        .exercise-card {
            border-left: 4px solid ${day.color};
            background: white;
            padding: 2rem;
            border-radius: 8px;
            margin: 2rem 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .code-block {
            background: #1e293b;
            color: #e2e8f0;
            padding: 1.5rem;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            margin: 1rem 0;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Navigation -->
        <nav class="day-nav">
            <a href="../index.html" class="nav-home">
                <i class="fas fa-home"></i>
            </a>
            <div class="day-progress">
                <span class="phase-banner">${day.phaseName}</span>
                <h1>Day ${day.day}: ${day.topic}</h1>
            </div>
            <div class="nav-controls">
                ${prevDay ? `<a href="day-${prevDay.toString().padStart(2, '0')}.html" class="btn-nav">
                    <i class="fas fa-arrow-left"></i> Day ${prevDay}
                </a>` : ''}
                ${nextDay ? `<a href="day-${nextDay.toString().padStart(2, '0')}.html" class="btn-nav">
                    Day ${nextDay} <i class="fas fa-arrow-right"></i>
                </a>` : ''}
            </div>
        </nav>

        <!-- Main Content -->
        <main class="day-content">
            <!-- Exercise Card -->
            <div class="exercise-card">
                <h2><i class="fas fa-flask"></i> Senior Exercise</h2>
                <p class="exercise-description">${day.exercise}</p>

                <!-- Example Code Block -->
                <div class="code-block">
                    <span style="color: #94a3b8;"># Example code for Day ${day.day}</span><br>
                    <span style="color: #60a5fa;">import</span> os<br>
                    <span style="color: #60a5fa;">import</span> sys<br>
                    <br>
                    <span style="color: #fbbf24;">def</span> <span style="color: #34d399;">main</span>():<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cbd5e1;">print</span>(<span style="color: #86efac;">"Day ${day.day}: ${day.topic}"</span>)
                </div>

                <!-- Objectives -->
                <div class="objectives">
                    <h3><i class="fas fa-bullseye"></i> Learning Objectives</h3>
                    <ul>
                        <li>Understand the fundamental concepts of ${day.topic.toLowerCase()}</li>
                        <li>Implement the exercise in a real-world scenario</li>
                        <li>Troubleshoot common issues and edge cases</li>
                        <li>Apply the knowledge to optimize data engineering workflows</li>
                    </ul>
                </div>
            </div>

            <!-- Quiz Section -->
            <div class="quiz-section">
                <h3><i class="fas fa-question-circle"></i> Knowledge Check</h3>
                <div class="quiz-question">
                    <p>What is the main concept being tested in this exercise?</p>
                    <div class="quiz-options">
                        <label>
                            <input type="radio" name="quiz-${day.day}" value="a">
                            ${day.topic} fundamentals
                        </label>
                        <label>
                            <input type="radio" name="quiz-${day.day}" value="b">
                            System design patterns
                        </label>
                        <label>
                            <input type="radio" name="quiz-${day.day}" value="c">
                            Performance optimization
                        </label>
                        <label>
                            <input type="radio" name="quiz-${day.day}" value="d">
                            All of the above
                        </label>
                    </div>
                    <button class="btn-submit" onclick="checkAnswer(${day.day})">Check Answer</button>
                </div>
            </div>

            <!-- Related Resources -->
            <div class="resources">
                <h3><i class="fas fa-book"></i> Related Resources</h3>
                <div class="resource-links">
                    <a href="../phases/${day.phase}.html" class="resource-link">
                        <i class="fas fa-layer-group"></i> Phase Overview
                    </a>
                    <a href="https://github.com/trivikrama1988/100-Days-of-Data-Engineering/tree/main/${day.phase}/day-${day.day.toString().padStart(2, '0')}-${day.topic.toLowerCase().replace(/\s+/g, '-')}"
                       class="resource-link" target="_blank">
                        <i class="fab fa-github"></i> Repository Files
                    </a>
                    <a href="#" class="resource-link" onclick="markComplete(${day.day})">
                        <i class="fas fa-check-circle"></i> Mark as Complete
                    </a>
                </div>
            </div>
        </main>

        <!-- Footer Navigation -->
        <footer class="day-footer">
            <div class="footer-nav">
                ${prevDay ? `<a href="day-${prevDay.toString().padStart(2, '0')}.html" class="btn-footer">
                    <i class="fas fa-arrow-left"></i> Previous: Day ${prevDay}
                </a>` : '<div></div>'}
                <a href="../days/index.html" class="btn-footer">
                    <i class="fas fa-list"></i> All Days
                </a>
                ${nextDay ? `<a href="day-${nextDay.toString().padStart(2, '0')}.html" class="btn-footer">
                    Next: Day ${nextDay} <i class="fas fa-arrow-right"></i>
                </a>` : '<div></div>'}
            </div>
            <div class="progress-indicator">
                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${day.day}%"></div>
                </div>
                <span>Progress: ${day.day}%</span>
            </div>
        </footer>
    </div>

    <script src="../assets/js/day-navigation.js"></script>
    <script>
        function checkAnswer(day) {
            const selected = document.querySelector(\`input[name="quiz-\${day}"]:checked\`);
            if (selected && selected.value === 'd') {
                alert('Correct! This exercise tests multiple aspects of data engineering.');
                saveProgress(day, 1);
            } else {
                alert('Please review the exercise objectives and try again.');
            }
        }

        function markComplete(day) {
            if (confirm('Mark Day ' + day + ' as completed?')) {
                saveProgress(day, 100);
                alert('Day ' + day + ' marked as complete!');
            }
        }

        function saveProgress(day, score) {
            const progress = JSON.parse(localStorage.getItem('de_progress') || '{}');
            progress['day' + day] = {
                completed: true,
                score: score,
                completedAt: new Date().toISOString()
            };
            localStorage.setItem('de_progress', JSON.stringify(progress));
        }
    </script>
</body>
</html>`;
}

function generateDaysIndexHTML(days) {
    const phases = {};
    days.forEach(day => {
        if (!phases[day.phase]) {
            phases[day.phase] = [];
        }
        phases[day.phase].push(day);
    });

    let html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Days - 100 Days of Data Engineering</title>
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <nav class="main-nav">
            <a href="../index.html" class="nav-home">
                <i class="fas fa-home"></i> Home
            </a>
            <h1>All 100 Days</h1>
        </nav>

        <div class="days-container">`;

    // Generate phase sections
    Object.keys(phases).forEach(phase => {
        const phaseDays = phases[phase];
        const phaseName = phaseDays[0].phaseName;
        const phaseColor = phaseDays[0].color;

        html += `
        <div class="phase-section" style="border-color: ${phaseColor};">
            <div class="phase-header" style="background: ${phaseColor};">
                <h2>${phaseName}</h2>
                <span>Days ${phaseDays[0].day} - ${phaseDays[phaseDays.length - 1].day}</span>
            </div>
            <div class="days-grid">`;

        phaseDays.forEach(day => {
            html += `
            <a href="day-${day.day.toString().padStart(2, '0')}.html" class="day-card">
                <div class="day-number">${day.day}</div>
                <h3>${day.topic}</h3>
                <p>${day.exercise.substring(0, 80)}...</p>
                <div class="day-meta">
                    <span class="status-indicator" data-day="${day.day}">
                        <i class="fas fa-circle"></i> Pending
                    </span>
                </div>
            </a>`;
        });

        html += `
            </div>
        </div>`;
    });

    html += `
        </div>
    </div>

    <script>
        // Load progress and update status indicators
        document.addEventListener('DOMContentLoaded', () => {
            const progress = JSON.parse(localStorage.getItem('de_progress') || '{}');

            document.querySelectorAll('.status-indicator').forEach(indicator => {
                const day = indicator.dataset.day;
                if (progress['day' + day]) {
                    indicator.innerHTML = '<i class="fas fa-check-circle"></i> Completed';
                    indicator.style.color = '#10b981';
                    indicator.closest('.day-card').style.opacity = '0.8';
                }
            });
        });
    </script>
</body>
</html>`;

    return html;
}