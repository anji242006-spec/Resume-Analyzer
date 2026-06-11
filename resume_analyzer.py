skills = ["Python", "AI", "Machine Learning", "Data Science", "SQL"]

resume_text = input("Paste your resume text:\n")

found_skills = []

for skill in skills:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)

print("\n=== Resume Analysis Report ===")

if found_skills:
    print("Skills Found:")
    for skill in found_skills:
        print("-", skill)
else:
    print("No matching skills found.")

print("\nTotal Skills Matched:", len(found_skills))
