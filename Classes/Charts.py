import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import os
from Classes.TypeOfAttendence import TypeOfAttendence

class Charts:
    output_dir = "charts_output"
    excel_file = os.path.join(output_dir, "charts_report.xlsx")

    @staticmethod
    def _prepare_output():
        os.makedirs(Charts.output_dir, exist_ok=True)

    @staticmethod
    def _save_chart_and_data(writer, image_path, sheet_name, dataframe: pd.DataFrame):
        dataframe.to_excel(writer, sheet_name=sheet_name[:31], startrow=15, index=False)
        workbook = writer.book
        worksheet = writer.sheets[sheet_name[:31]]
        worksheet.insert_image('B2', image_path)

    @staticmethod
    def plot_student_averages(students: list, writer):
        names = []
        averages = []
        for student in students:
            try:
                avg = student.avarage()
                names.append(f"{student.name} {student.lastName}")
                averages.append(avg)
            except:
                continue

        df = pd.DataFrame({"Name": names, "Average": averages})

        plt.figure()
        plt.bar(names, averages)
        plt.title("Średnia ocen uczniów")
        plt.ylabel("Średnia")
        plt.xticks(rotation=45)
        plt.tight_layout()
        image_path = os.path.join(Charts.output_dir, "student_averages.png")
        plt.savefig(image_path)
        plt.close()

        Charts._save_chart_and_data(writer, image_path, "Srednie", df)

    @staticmethod
    def plot_attendance_distribution(students: list, writer):
        attendance_types = ["PRESENT", "LATE", "NOTPRESENT"]
        summary = {f"{s.name} {s.lastName}": {t: 0 for t in attendance_types} for s in students}

        for student in students:
            for att in student.attendance:
                typ = att.typeOfAttendence.name
                if typ in summary[f"{student.name} {student.lastName}"]:
                    summary[f"{student.name} {student.lastName}"][typ] += 1

        df = pd.DataFrame(summary).T.reset_index().rename(columns={"index": "Student"})

        ax = df.set_index("Student").plot(kind="bar", stacked=True, title="Obecność uczniów")
        ax.set_ylabel("Liczba wpisów")
        plt.xticks(rotation=45)
        plt.tight_layout()
        image_path = os.path.join(Charts.output_dir, "attendance_distribution.png")
        plt.savefig(image_path)
        plt.close()

        Charts._save_chart_and_data(writer, image_path, "Obecnosc", df)

    @staticmethod
    def plot_student_grades_over_time(student, writer):
        if not student.grades:
            print(f"Uczeń {student.name} {student.lastName} nie ma ocen.")
            return

        dates = [g.date for g in student.grades]
        grades = [g.grade for g in student.grades]
        df = pd.DataFrame({"Date": dates, "Grade": grades})

        plt.figure()
        plt.plot(dates, grades, marker='o')
        plt.title(f"Trend ocen - {student.name} {student.lastName}")
        plt.xlabel("Data")
        plt.ylabel("Ocena")
        plt.grid(True)
        plt.tight_layout()
        image_path = os.path.join(Charts.output_dir, f"grades_{student.name}_{student.lastName}.png")
        plt.savefig(image_path)
        plt.close()

        Charts._save_chart_and_data(writer, image_path, f"Oceny_{student.name}_{student.lastName}"[:31], df)

    @staticmethod
    def export_all(students: list):
        Charts._prepare_output()
        with pd.ExcelWriter(Charts.excel_file, engine='xlsxwriter') as writer:
            Charts.plot_student_averages(students, writer)
            Charts.plot_attendance_distribution(students, writer)
            for student in students:
                Charts.plot_student_grades_over_time(student, writer)
        print(f"Wszystkie dane i wykresy zapisano do: {Charts.excel_file}")
