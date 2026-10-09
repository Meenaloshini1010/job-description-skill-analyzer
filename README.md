# Job Description Skill Analyzer

## About the Project

The Job Description Skill Analyzer is a Python-based web application that compares the skills required in a job description with the skills provided by a candidate.

It identifies matched skills, missing skills, and calculates an overall skill match percentage.

## Features

* Job description input
* Candidate skill input
* Required skill extraction using predefined keywords
* Matched and missing skill identification
* Skill match percentage calculation
* Input validation
* Web interface built with HTML and CSS

## Technologies Used

* Python
* Flask
* HTML
* CSS

## Project Structure

* `app.py` — Flask application and analysis logic
* `skill_analyzer.py` — Original Python console version
* `templates/index.html` — Webpage structure
* `static/style.css` — Webpage styling

## How to Run

1. Install Python.

2. Install Flask:

   `python -m pip install flask`

3. Open a terminal in the project folder.

4. Run:

   `python app.py`

5. Open the local address displayed in the terminal, usually `http://127.0.0.1:5000/`.

## Limitation

The current version uses a predefined list of skills and basic keyword matching. It may not recognize every skill or variation in a job description.
