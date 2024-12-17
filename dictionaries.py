courses = {
    "institution": "UCEN",
    "city": "Manchester",
    "locations": "CCM",
    "course list": [
        "BSc in Designing",
        "BSc in Networking",
        "BSc in Software Development",
        "FDSc in Cyber Security",
        "BSc in Social Science"
    ]
}

print(courses)
print(courses["institution"], courses["city"], courses["locations"])

for course in courses["course list"]:
    print(f"{courses['institution']} offers a course called {course}")
