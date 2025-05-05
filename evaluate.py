from recommendation_engine import recommend_assessments

# Test dataset (ground truth)
samples = [
    {"job_role": "Software Developer", "skills": ["Problem Solving", "Coding"], "true": ["Cognitive Ability Test", "Coding Simulation"]},
    {"job_role": "Sales", "skills": ["Leadership", "Communication"], "true": ["Personality Questionnaire"]},
]

correct = 0
total = 0

for sample in samples:
    predicted = recommend_assessments(sample["job_role"], sample["skills"])
    for item in sample["true"]:
        total += 1
        if item in predicted:
            correct += 1

accuracy = correct / total
print(f"Accuracy: {accuracy:.2f}")
