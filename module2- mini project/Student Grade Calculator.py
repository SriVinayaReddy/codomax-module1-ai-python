# CODOMAX Internship - Module 2
# Project 3: Student Grade Calculator

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"
 
 
def student_grade_calculator():
    print("=== Student Grade Calculator ===")
    students = {}
 
    num_students = int(input("How many students? "))
 
    for _ in range(num_students):
        name = input("\nEnter student name: ")
        num_subjects = int(input(f"How many subjects for {name}? "))
        marks = []
 
        for i in range(num_subjects):
            mark = float(input(f"  Enter marks for subject {i + 1}: "))
            marks.append(mark)
 
        average = sum(marks) / len(marks)
        grade = get_grade(average)
        students[name] = {"marks": marks, "average": average, "grade": grade}
 
    # Display results sorted by average (highest first)
    print("\n=== Results ===")
    ranked = sorted(students.items(), key=lambda x: x[1]["average"], reverse=True)
 
    for rank, (name, data) in enumerate(ranked, start=1):
        print(f"Rank {rank}: {name} | Average: {data['average']:.2f} | Grade: {data['grade']}")
 
 
if __name__ == "__main__":
    student_grade_calculator()
 