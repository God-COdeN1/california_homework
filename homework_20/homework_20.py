class Man:
    _salary = "1500 - 10000"

    def __init__(self, name, last_name, age, passport_num):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.__passport_num = passport_num

    def sleep(self):
        return f"Good nigh {self.name}"

    @staticmethod
    def count(salary_in_hour, work_time):
        return salary_in_hour * work_time


class Women(Man):
    super.__init__
    _salary = "500 - 5000"


man = Man(name="Piter", last_name="Parker", age=29, passport_num=45534676586)
women = Women(name="Alice", last_name="Parker", age=26, passport_num=45534656386)

# alice.sleep()
tuples = (1, 1, 2, 3, 3, 4, 5)

print(tuples)
print(tuples.count(3))
print(Women.count(salary_in_hour=20, work_time=4))
