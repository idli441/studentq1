def student_analysis():
    students = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\nDetails for student {i+1}:")
        data = input().split()
        name, roll, dept, addr, gender = data[:5]
        marks = list(map(int, data[5:]))
        total = sum(marks)
        percentage = total / len(marks)
        students.append((name, roll, dept, addr, gender, marks, total, percentage))

    students.sort(key=lambda x: x[6])
    print("\nSorted Students:")
    for s in students:
        print(f"{s[0]} - Total: {s[6]}, %: {s[7]:.2f}")

    print(f"\nTopper: {students[-1][0]}")
    print(f"Lowest scorer: {students[0][0]}")
    print(f"Failed students: {[s[0] for s in students if min(s[5]) < 10]}")

def main():
    print("=== Student Details and Analysis ===")
    student_analysis()

if __name__ == "__main__":
    main()
