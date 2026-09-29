students = {
    "S101": {"name": "Omkar Kharat","attendance": {"Python": [42, 50],"Mathematics": [45, 50],"English": [38, 45],"EVS": [40, 50],"Physics": [43, 50]}},
    "S102": {"name": "Yash Ghodke","attendance": {"Python": [48, 50],"Mathematics": [47, 50],"English": [43, 45],"EVS": [46, 50],"Physics": [49, 50]}},
    "S103": {"name": "Ganesh Reddy","attendance": {"Python": [35, 50],"Mathematics": [32, 50],"English": [36, 45],"EVS": [38, 50],"Physics": [34, 50]}},
    "S104": {"name": "Dhurv Kumar","attendance": {"Python": [44, 50],"Mathematics": [40, 50],"English": [41, 45],"EVS": [45, 50],"Physics": [42, 50]}}
    }
def percentage(attended, total):
    if total == 0:
        return 0
    return (attended / total) * 100
def status(percentage):
    if percentage >= 75:
        return "ELIGIBLE"
    else:
        return "SHORTAGE"
def report(id):
    if id not in students:
        print("\n id not found")
        return
    student = students[id]
    print(" STUDENT ATTENDANCE REPORT")
    print("Student ID :", id)
    print("Name       :", student["name"])
    total_attended = 0
    total_classes = 0
    print("Subject wise Attendance")
    for i, x in student["attendance"].items():
        attended = x[0]
        total = x[1]
        percentage = percentage(attended, total)
        status = status(percentage)
        print("Subject :", i)
        print("Attended:", attended, "/", total)
        print("Percentage:",percentage, "%")
        print("Status:", status)
        total_attended += attended
        total_classes += total
    overall_percentage = percentage(total_attended,total_classes)
    print("Total Classes   :", total_classes)
    print("Classes Attended:", total_attended)
    print("Overall Attendance:",overall_percentage, "%")
    print("Overall Status   :",status(overall_percentage))
def calculate_shortage(id):
    if id not in students:
        print("id not found")
    student = students[id]
    print("ATTENDANCE SHORTAGE")
    for subject, data in student["attendance"].items():
        attended = data[0]
        total = data[1]
        percentage = percentage(attended, total )
        if percentage < 75:
            required = 0
            temp_attended = attended
            temp_total = total
            while (temp_attended / temp_total) * 100 < 75:
                temp_total += 1
                temp_attended += 1
                required += 1
            print(
                f"{subject}: {percentage}% "
                f" Attend {required} more class(es)"
            )
        else:
            print(
                f"{subject}: {percentage}% "
                "No shortage"
            )
def class_analysis():
    print("CLASS ANALYSIS")
    total_attended = 0
    total_classes = 0
    for id, j in students.items():
        attended = 0
        classes = 0
        for data in j["attendance"].values():
            attended += data[0]
            classes += data[1]
        percentage = percentage(attended,classes)
        print(f"{id} {j['name']}: "f"{percentage}%")
        t1+= attended
        t2 += classes
    class_percentage = percentage(t1,t2)
    print("Overall Class Attendance:",(percentage), "%")
def main():
    while True:
        print("STUDENT ATTENDANCE CALCULATOR")
        print("1. Student Attendance Report")
        print("2. Attendance Shortage")
        print("3. Class Attendance Analysis")
        print("4. Display All Students")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            id = input("Enter Student ID: ")
            report(id)
        elif choice == 2:
            id = input("Enter Student ID: ")
            calculate_shortage(id)
        elif choice == 3:
            class_analysis()
        elif choice == 4:
            for id in students:
                report(id)
        elif choice == 5:
            print("Thank you ")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

