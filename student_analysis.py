def student_analysis():
    students = []
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        print(f"\nEnter details for student {i + 1}:")
        name = input("Name: ")
        roll = input("Roll No: ")
        dept = input("Department: ")
        addr = input("Address: ")
        gender = input("Gender: ")
        
        num_subjects = int(input("Number of subjects: "))
        marks = []
        for j in range(num_subjects):
            mark = int(input(f"Enter mark for subject {j + 1}: "))
            marks.append(mark)
        
        total = sum(marks)
        percentage = total / len(marks)
        
        students.append((name, roll, dept, addr, gender, marks, total, percentage))

    # Sort students by total marks
    students.sort(key=lambda x: x[6])

    print("\n=== Sorted Students by Total Marks ===")
    for s in students:
        print(f"{s[0]} - Total: {s[6]}, Percentage: {s[7]:.2f}%")

    print(f"\nTopper: {students[-1][0]}")
    print(f"Lowest scorer: {students[0][0]}")
    
    # Check for failed students (any subject < 10)
    failed = [s[0] for s in students if min(s[5]) < 10]
    if failed:
        print("Failed students:", failed)
    else:
        print("No failed students.")

def main():
    print("=== Student Details and Analysis ===")
    student_analysis()

if __name__ == "__main__":
    main()
