class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name        = name
        self.roll_number = roll_number
        self.cgpa        = cgpa

def sort_students(student_list):
    return sorted(student_list, key=lambda x: x.cgpa, reverse=True)

# Test the function
if __name__ == "__main__":
    # Example usage
    students = [
        Student("Deepika"  , "001", 3.8),
        Student("Aarthi"    , "002", 3.6),
        Student("Ashmitha", "003", 3.9),
        Student("Banu"  , "004", 3.7),
    ]

    sorted_students = sort_students(students)

    # Print sorted students
    for student in sorted_students:
        print(f"\nName        : {student.name}   \nRoll Number : {student.roll_number} \nCGPA        : {student.cgpa}")
