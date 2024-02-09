
from models.models import StudentDailyAssessment


class DataRepo:
    @staticmethod
    def save_data_to_file(data, filename):
        with open(filename, 'a') as file:
            for item in data:
                file.write(f"{item.name},{item.date},{item.on_time},{item.consistent},{item.partial},{item.minutes},{item.final_score}\n")

    @staticmethod
    def load_data_from_file(filename):
        data = []
        with open(filename, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                name = fields[0]
                date = fields[1]
                on_time = fields[2]
                consistent = fields[3]
                partial = fields[4]
                minutes = fields[5]
                final_score = fields[6]
                data.append(StudentDailyAssessment(name, date, on_time, consistent, partial, minutes, final_score))
        return data
