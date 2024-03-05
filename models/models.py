
class StudentDailyAssessment(object):
    def __init__(self, name, date, on_time, consistent, partial, minutes, final_score):
        self.name = name
        self.date = date
        self.on_time = on_time
        self.consistent = consistent
        self.partial = partial
        self.minutes = minutes
        self.final_score = final_score

    def display_result(self):
        print(f"Name: {self.name}")
        print(f"Day score: {self.final_score}")

    def absolute_points(self):
        base_points = 750
        if self.on_time:
            base_points += 100
        if self.consistent:
            base_points += 100
        if self.partial:
            base_points -= 150
        self.final_score = base_points
