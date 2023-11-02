class Worker:
    max_income_in_hour = 1_000
    min_income_in_hour = 10

    def __init__(self, income_in_hour, work_time, position):
        self.income_in_hour = int(income_in_hour)
        self.work_time = int(work_time)
        self.position = position

    def income_per_day(self):
        if self.work_time <= 24:
            return f"{self.work_time * self.income_in_hour}$ per day"
        else:
            return "Incorrect time"

    @staticmethod
    def income_per_day_calculator(income_in_hour, work_time):
        return int(income_in_hour) * int(work_time)

    """
        min_or_max_salary func have 1 and 2 mode
        """

    @classmethod
    def min_or_max_salary(cls, work_time, mode=1):
        if mode == 1:
            return work_time * cls.max_income_in_hour
        elif mode == 2:
            return work_time * cls.min_income_in_hour


print(Worker.income_per_day_calculator(20, 8))
# Dima = Worker(34, 8, "secretary")
# print(Dima.income_per_day())
