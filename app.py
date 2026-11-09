from student import get_student, calculate_average


def main():

    student = get_student(2)

    if student:
        print("Student:", student["name"])
        print("Marks:", student["marks"])

    print("Average marks:", calculate_average())


if __name__ == "__main__":
    main()