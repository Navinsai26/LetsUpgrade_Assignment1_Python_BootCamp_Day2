def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
        return "D"
    else:
        return "Fail"

def main():
    while True:
        try:
            marks = float(input("Enter the marks obtained by the student: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if 0 <= marks <= 100:
            grade = calculate_grade(marks)
            print(f"The grade for the student is: {grade}")
        else:
            print("Invalid marks. Marks should be between 0 and 100.")
        
        another_student = input("Do you want to calculate the grade for another student? (yes/no): ").lower()
        if another_student != "yes":
            break

if __name__ == "__main__":
    main()
