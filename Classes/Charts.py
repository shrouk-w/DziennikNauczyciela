import matplotlib.pyplot as plt
from datetime import datetime
from Classes.TypeOfAttendence import TypeOfAttendence

class Charts:
    @staticmethod
    def plot_student_averages(students: list):
        names = []
        averages = []
        for student in students:
            try:
                avg = student.avarage()
                names.append(f"{student.name} {student.lastName}")
                averages.append(avg)
            except:
                continue

        plt.figure()
        plt.bar(names, averages)
        plt.title("Średnia ocen uczniów")
        plt.ylabel("Średnia")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_attendance_distribution(students: list):
        attendance_types = ["PRESENT", "LATE", "NOTPRESENT"]
        summary = {f"{s.name} {s.lastName}": {t: 0 for t in attendance_types} for s in students}

        for student in students:
            for att in student.attendance:
                typ = att.typeOfAttendence.name
                if typ in summary[f"{student.name} {student.lastName}"]:
                    summary[f"{student.name} {student.lastName}"][typ] += 1

        import pandas as pd
        df = pd.DataFrame(summary).T
        df.plot(kind="bar", stacked=True)
        plt.title("Obecność uczniów")
        plt.ylabel("Liczba wpisów")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_student_grades_over_time(student):
        if not student.grades:
            print("Uczeń nie ma ocen.")
            return

        dates = [g.date for g in student.grades]
        grades = [g.grade for g in student.grades]

        plt.figure()
        plt.plot(dates, grades, marker='o')
        plt.title(f"Trend ocen - {student.name} {student.lastName}")
        plt.xlabel("Data")
        plt.ylabel("Ocena")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
