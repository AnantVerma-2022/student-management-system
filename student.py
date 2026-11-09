students = [
    {"id": 1, "name": "Rahul", "marks": 85},
    {"id": 2, "name": "Priya", "marks": 90},
    {"id": 3, "name": "Amit", "marks": 75}
]


def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def calculate_average():
    total = sum(s["marks"] for s in students)

    # Intentional bug
    return total / len(student)