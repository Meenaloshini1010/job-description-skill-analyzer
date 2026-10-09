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

# Get Job Description
job_description = input("Enter the Job Description: ")

# Clean Job Description
job_description = job_description.lower()
job_description = job_description.replace(",", " ")

# Find required skills
matched_skills = []

for skill in skills:
    if f" {skill} " in f" {job_description} ":
        matched_skills.append(skill)

# Get candidate skills
candidate_input = input("Enter your skills: ")

candidate_skills = candidate_input.lower().replace(",", " ").split()

# Find candidate's matched skills
candidate_matched = []

for skill in matched_skills:
    if skill in candidate_skills:
        candidate_matched.append(skill)

# Find candidate's missing skills
candidate_missing = []

for skill in matched_skills:
    if skill not in candidate_skills:
        candidate_missing.append(skill)

# Calculate match percentage
if len(matched_skills) > 0:
    match_percentage = (len(candidate_matched) / len(matched_skills)) * 100
else:
    match_percentage = 0

# Display results
print("\n========================================")
print("       JOB DESCRIPTION SKILL ANALYZER")
print("========================================")

print("\nRequired Skills:")
print(", ".join(matched_skills))

print("\nCandidate Skills:")
print(", ".join(candidate_skills))

print("\nMatched Skills:")
print(", ".join(candidate_matched))

print("\nMissing Skills:")
print(", ".join(candidate_missing))

print("\nMatch Percentage:", round(match_percentage, 2), "%")

print("\n========================================")