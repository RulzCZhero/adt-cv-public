import sys
import os

def analyzeData(analytics: str,course: str,output :str) -> None:
    students = {}
    atRisk = []
    totalScores = 0.0
    totalStudents = 0
    with open(analytics, "r", encoding="utf-8") as f, open(output,"w",encoding="utf-8") as out:
        for line in f:
            temp = line.split(";")
            if course.lower() in temp[0].lower():
                if temp[1] not in students or (temp[1] in students and students[temp[1]]<float(temp[2])):
                    students[temp[1]] = float(temp[2])
        for student in students.items():
            totalStudents+=1
            totalScores+=float(student[1])
            if float(student[1]) <50:
                atRisk.append(student[0])
        if(totalStudents>0):
            out.write(f"Course Report: {course}\n")
            out.write("----------------------\n")
            out.write(f"Total Students: {totalStudents}\n")
            out.write(f"Success Rate: {((totalStudents-len(atRisk))/totalStudents)*100}%\n")
            out.write(f"Average Best Score: {round(totalScores/totalStudents,1)}\n")
            out.write("\n")
            out.write("At Risk Students:\n")
            if len(atRisk) > 0:
                for student in atRisk:
                    out.write(f"{student}\n")
            else:
                out.write("None")
        print("Analytics created!")
        table = input("Would you like to print a table of grades? (Y/N)")
        if table.lower() == "y":
            tablePrinter(students,course)  

def tablePrinter(students: dict, course: str) -> None:
    gradesInOrder = []
    for student in students.items():
        if student[1] <50:
            gradesInOrder.append("F")
        elif student[1] <74:
            gradesInOrder.append("C")
        elif student[1] <89:
            gradesInOrder.append("B")
        elif student[1] <=100:
            gradesInOrder.append("A")
    print(f"RESULTS FOR COURSE: {course}")
    print(f"------------------------------")
    print(f"STUDENT ID | POINTS | GRADE")
    print(f"------------------------------")
    for i,student in enumerate(students.items()):
        print(f"{student[0]:<11}| {student[1]:<7}| {gradesInOrder[i]}")
    print(f"------------------------------")



def main():
    if len(sys.argv)<4:
        print("You are missing some arguments")
        print("Usage: python analytics.py <input_file> <course_name> <output_file>")
        sys.exit(1)
    analytic = sys.argv[1]
    course = sys.argv[2]
    output = sys.argv[3]
    if os.path.exists(analytic):
        analyzeData(analytic,course,output)
    else:
        print(f"file {analytic} does not exist.")

if __name__ == '__main__':
    main()