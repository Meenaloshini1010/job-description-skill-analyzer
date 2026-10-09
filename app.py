from flask import Flask, render_template, request

app = Flask(__name__)


# Skills supported by the analyzer
skills = [
    "python",
    "sql",
    "mysql",
    "excel",
    "power bi",
    "tableau",
    "java",
    "c",
    "c++",
    "javascript",
    "html",
    "css",
    "flask",
    "git",
    "github",
    "aws",
    "azure",
    "linux",
    "docker"
]


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Get input from the form
        job_description = request.form.get("job_description", "")
        candidate_skills = request.form.get("candidate_skills", "")

        # Remove unnecessary spaces
        job_description = job_description.strip()
        candidate_skills = candidate_skills.strip()

        # --------------------------------
        # VALIDATION 1: EMPTY INPUT
        # --------------------------------

        if not job_description or not candidate_skills:

            return render_template(
                "index.html",
                error="Please enter both the job description and your skills."
            )


        # --------------------------------
        # PROCESS JOB DESCRIPTION
        # --------------------------------

        job_description = job_description.lower()

        job_description = job_description.replace(",", " ")
        job_description = job_description.replace(".", " ")


        # --------------------------------
        # FIND REQUIRED SKILLS
        # --------------------------------

        matched_skills = []

        for skill in skills:

            if f" {skill} " in f" {job_description} ":
                matched_skills.append(skill)


        print("Required Skills:", matched_skills)


        # --------------------------------
        # VALIDATION 2:
        # NO RECOGNIZED SKILLS
        # --------------------------------

        if len(matched_skills) == 0:

            return render_template(
                "index.html",
                error="No recognized skills were found in the job description. Please enter a job description containing supported skills."
            )


        # --------------------------------
        # PROCESS CANDIDATE SKILLS
        # --------------------------------

        candidate_skills = (
            candidate_skills
            .lower()
            .replace(",", " ")
            .split()
        )

        print("Candidate Skills:", candidate_skills)


        # --------------------------------
        # FIND MATCHED SKILLS
        # --------------------------------

        candidate_matched = []

        for skill in matched_skills:

            if skill in candidate_skills:
                candidate_matched.append(skill)

        print("Matched Skills:", candidate_matched)


        # --------------------------------
        # FIND MISSING SKILLS
        # --------------------------------

        candidate_missing = []

        for skill in matched_skills:

            if skill not in candidate_skills:
                candidate_missing.append(skill)

        print("Missing Skills:", candidate_missing)


        # --------------------------------
        # CALCULATE MATCH PERCENTAGE
        # --------------------------------

        match_percentage = (
            len(candidate_matched)
            / len(matched_skills)
        ) * 100

        print(
            "Match Percentage:",
            round(match_percentage, 2),
            "%"
        )


        # --------------------------------
        # SEND RESULTS TO HTML
        # --------------------------------

        return render_template(
            "index.html",
            required_skills=matched_skills,
            candidate_skills=candidate_skills,
            matched_skills=candidate_matched,
            missing_skills=candidate_missing,
            match_percentage=round(match_percentage, 2)
        )


    # First time opening the webpage
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)