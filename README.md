# Production Engineering - Week 1 - Portfolio Site

## Inspiration
We wanted to build a portfolio website that matched Pod pride as Python Pythons, which is why we went for the jungle-inspired look!

## Installation

### Mac
1. Clone the repo via ssh: `git clone git@github.com:MLH-Fellowship/project-team-jungle.git`

2. Create a virtual environment with venv: `python3 -m venv`

3. Activate the virtual environment: `source venv/bin/activate`

4. Install dependencies: `pip3 install -r requirements.txt`

5. Run Flask server: `flask run`

6. Go to `http://127.0.0.1:5000/` in the browser

## What it does
A portfolio website showcasing our team's profiles, hobbies, work experiences, and projects. We also have a cool map to show call the unique locations we have visited all over the globe! Our priority was for the site to be modular so that anyone could add their own information and showcase their profiles using this template. Therefore, all personal information is extracted from a JSON file where end users could fill out the required fields. 

## How we built it
- Flask
- Jinja
- Folium
- HTML
- CSS
- JavaScript
- Bootstrap V5.0

## Challenges we ran into
- Setting up flask server 
- Folium not insertable with Jinja templates

## Accomplishments that we're proud of
- Sticking completely to the theme
- Being comfortable with branches, and merge conflicts
- Following good practices for naming and reviewing PRs

## What we learned
-  Using Flask and Jinja templating when working on this project
-  How to use Folium for our map framework
- Customizing Bootstrap elements for a cohesive theme

## What's next for Team Jungle
Connect to a database, and automate the process for making updates to hobbies, experiences, and locations visited so that users can add information to the site through a graphical user interface.
