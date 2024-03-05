
from datetime import date, timedelta

from models.models import StudentDailyAssessment
from repo.repo import DataRepo
from utils.utils import input_to_bool


def relative_points(student_perform_list: [StudentDailyAssessment]):
    max_relative_score = 50
    participants_time_list = map(
        lambda s_student: s_student.minutes,
        student_perform_list
        )
    max_time = max(participants_time_list)

    for single_student in student_perform_list:
        single_student.final_score += int(max_relative_score * (single_student.minutes / max_time))
        single_student.final_score = single_student.final_score / 10


if __name__ == '__main__':

    session_date = date.today() - timedelta(days=1)
    student_performance_list = []

    # While statement housekeeping code
    continue_condition = True
    i = 0

    while continue_condition:
        print(f"Student {i + 1}")
        name_input = input('What is the student name?: ')
        on_time_input = input_to_bool(input('Was the student on time? (y/n): '))
        consistent_input = input_to_bool(input('Was the student consistent? (y/n): '))
        partial_input = input_to_bool(input('Was the student partial? (y/n): '))
        minutes_input = int(input('How many minutes of study were accomplished?: '))

        student_performance_list.append(
            StudentDailyAssessment(
                name_input,
                session_date,
                on_time_input,
                consistent_input,
                partial_input,
                minutes_input,
                -1
            )
        )
        student_performance_list[-1].absolute_points()
        i += 1

        condition_input = input_to_bool(input("Do you want to continue adding students? (y/n): "))
        if not condition_input:
            continue_condition = False

    relative_points(student_performance_list)

    DataRepo.save_data_to_file(student_performance_list, 'history_repo.txt')

    print('\n***************************************************************')
    print(f'****************** RESULTS: Date: {session_date} ******************')
    print('***************************************************************\n')
    for student in student_performance_list:
        student.display_result()
