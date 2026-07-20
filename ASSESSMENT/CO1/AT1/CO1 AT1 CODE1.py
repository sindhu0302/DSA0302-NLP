import re

# Sample resumes
resumes = [
"""
Name: John Smith
Email: john@gmail.com
Phone: 9876543210
Skills: Python, Java, SQL
Experience: 3 years
""",

"""
Name: Priya
Email: priya@yahoo.com
Phone: 9123456789
Skills: Java, SQL
Experience: 1 year
"""
]

skills_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]

print("Resume Information")

for resume in resumes:

    name = re.search(r"Name:\s*(.*)", resume).group(1)
    email = re.search(r"\S+@\S+", resume).group()
    phone = re.search(r"\d{10}", resume).group()
    exp = int(re.search(r"\d+", re.search(r"Experience:.*", resume).group()).group())

    skills = []
    for skill in skills_list:
        if re.search(skill, resume, re.IGNORECASE):
            skills.append(skill)

    print("\nName:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("Skills:", ", ".join(skills))
    print("Experience:", exp, "Years")

    if exp >= 2 and "Python" in skills:
        print("Status: Eligible")
    else:
        print("Status: Not Eligible")
