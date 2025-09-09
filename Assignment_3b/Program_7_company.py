
from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        return "EmployeeId: " + self.employeeId + "\n" + "Name :" + self.name + "\n"

    @abstractmethod
    def calculate_salary(self):
        pass

class PartTimeEmployee(Employee):

    def __init__(self, employee_id, name, hourly_rate, hours_worked):
        super().__init__(employee_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class FullTimeEmployee(Employee):

    def __init__(self, employee_id, name, salary):
        super().__init__(employee_id, name)
        self.salary = salary

    def calculate_salary(self):
        return 12 * self.salary


class ContractEmployee(Employee):

    def __init__(self, employee_id, name, salary, contract_period):
        super().__init__(employee_id, name)
        self.salary = salary
        self.contract_period = contract_period

    def calculate_salary(self):
        return self.contract_period * self.salary


def main():

    fte = FullTimeEmployee(1, "barane", 12000)
    pte = PartTimeEmployee(2, "kumar", 500, 20)
    ce = ContractEmployee(3, "kk", 7000, 7)

    print("Full Time Employee's salary: ", fte.calculate_salary())
    print("Part Time Employee's salary: ", pte.calculate_salary())
    print("Contract Employee's salary : ", ce.calculate_salary())


if __name__ == "__main__":
    main()