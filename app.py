from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Global projects list for the portfolio; change or extend as you add projects
PROJECTS = [
    {
        "title": "ARDUINO TETRIS GAME",
        "slug": "tetris-tower",
        "image": "/static/images/tetris.svg",
        "description": "Work in progress Tetris game I am building using The MAX7219 LED Matrix and a joystick",
        "long_description": "A handheld Tetris implementation using MAX7219-driven LED matrices and a joystick for controls. Current progress: hardware wiring and basic falling-block logic. Planned features include scoring, levels, and compact enclosure builds.",
        "tech": ["Arduino Uno", "MAX7219 LED Matrix", "C/C++", "Breadboard"],
        "repo": "https://github.com/yourusername/tetris-tower",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    },
    {
        "title":"Portfolio Website",
        "slug":"Portfolio",
        "image":"/static/images/portfolioHeader.jpg",
        "description": "A Small portfolio I created in order to showcase the Silly / Cool Things I decide to engineer",
        "long_description": "A portfolio that was born out of the suggestion of a professor when I asked him 'whats next?' He brought up making some sort of website using the Python skills we had aquired through out our course. This portfolio was built using the miniframe work called Flask, and basic HTML/CSS. This was a lot of fun to put together despite it being something very janky. I am also using this portfolio as an excuse to start uploading videos regarding engineerig projects. My biggest takeaway from this whole project is that I do NOT want to build websites as a career. Do not reach out for a website because I have no clue on what it is I am doing :)",
        "tech": ["Flask","HTML/CSS"],
        "repo":"https://github.com/yourusername/robot-demo",
    }
    
]

@app.route('/projects')
def projects_only():
    return render_template('Project_only_Page.html', projects=PROJECTS)

# This is your "About Me" tab (Home)
@app.route('/')
def home():
    # SITE: render homepage and pass the small PROJECTS list for the Projects section
    return render_template('home.html', projects=PROJECTS)


@app.route('/project/<slug>')
def project_detail(slug):
    # Find project by slug and render its detail page
    project = next((p for p in PROJECTS if p.get('slug') == slug), None)
    if not project:
        return "Project not found", 404
    
    # Pass all projects except the current one
    other_projects = [p for p in PROJECTS if p.get('slug') != slug]
    return render_template('project.html', project=project, other_projects=other_projects)

# This is your "Resume" tab
@app.route('/resume')
def resume():
    return redirect(url_for('home') + '#resume')

# This is your "Projects" tab
@app.route('/projects')
def projects():
    return redirect(url_for('home') + '#projects')


@app.route('/contact')
def contact():
    return redirect(url_for('home') + '#contact')


if __name__ == '__main__':
    app.run(debug=True)