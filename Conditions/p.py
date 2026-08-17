students = ['Bilal', 'Aisha', 'Abdullah']
scores = [89, 74, 95]
for student, score in zip(students, scores):
    if score >= 90:
        score = "Excellence"
    elif score > 79:
        score = 'Merit'
    elif score > 49:
        score = 'Pass'
    else:
        score = 'Fail'

    print(f"{student}: {score}")
    