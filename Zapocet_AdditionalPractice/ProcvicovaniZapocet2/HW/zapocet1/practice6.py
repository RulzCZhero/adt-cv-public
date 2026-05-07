def get_scholarship_winners(data) -> list[str]:
    scholarships = []
    for n in data:
        if 5 not in n["grades"] and n["credits"] >=20 and sum(n["grades"])/len(n["grades"])<=1.5:
            scholarships.append(n["name"])
    return scholarships


def main():
    students = [
    {"name": "Alice", "grades": [1, 2, 1, 1], "credits": 20},
    {"name": "Bob", "grades": [3, 4, 1, 2], "credits": 15},
    {"name": "Cyril", "grades": [1, 1, 1, 2], "credits": 25},
    {"name": "Dan", "grades": [5, 1, 2, 3], "credits": 20}
]
    print(f"These students are eligable for a scholarship: {get_scholarship_winners(students)}")
    

if __name__ == '__main__':
    main()