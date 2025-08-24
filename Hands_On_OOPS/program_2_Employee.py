
class Employee:

    def __init__(self, name, salary, work_hours):
        self.__name = name
        self.__salary = salary
        self.__work_hours = work_hours


    """Adds 10 to salary to employee when salary < 500"""
    def add_sal(self):
        if self.__salary < 500:
            self.__salary += 10

    """Adds 5 to salary to employee when work hours > 6"""
    def add_work(self):
        if self.__work_hours > 6:
            self.__salary += 5

    """return the total salary for the employee for a year"""
    def get_annual_salary(self):
        return 12 * self.__salary

def main():

    emp = Employee(name="Barane", salary=1000, work_hours=7)
    emp.add_work()

    print("Annual Salary: ", emp.get_annual_salary())

if __name__ == "__main__":
    main()