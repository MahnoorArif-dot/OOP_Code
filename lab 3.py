class Employee:
    def __init__(self, empNo, name, cnic, phone, address):
        self.empno = empNo
        self.name = name
        self.cnic = cnic
        self.phone = phone
        self.address = address


class Salaried(Employee):
    def __init__(self, empNo, name, cnic, phone, address, weeklysalary):
        super().__init__(empNo, name, cnic, phone, address)
        self.weeklysalary = weeklysalary

    def calculate_pay(self):
        return self.weeklysalary


class Hourly(Employee):
    def __init__(self, empNo, name, cnic, phone, address, hourwork, rph):
        super().__init__(empNo, name, cnic, phone, address)
        self.hourwork = hourwork
        self.rph = rph

    def calculate_pay(self):
        if self.hourwork > 40:
            regular_pay = self.rph * 40
            overtime_pay = (self.hourwork - 40) * (self.rph * 1.5)
            return regular_pay + overtime_pay
        else:
            return self.hourwork * self.rph


class Commission(Employee):
    def __init__(self, empNo, name, cnic, phone, address, salestotal, percentage):
        super().__init__(empNo, name, cnic, phone, address)
        self.salestotal = salestotal
        self.percentage = percentage

    def calculate_pay(self):
        return self.salestotal * (self.percentage / 100)


class Payroll:
    def __init__(self):
        self.employees = []

    def add_emp(self, s):
        self.employees.append(s)

    def total_pay(self):
        total = 0
        for employee in self.employees:
            total = total + employee.calculate_pay()
        return total


def main():
    p = Payroll()
    s = Salaried(1, "lubaba", "36601000", "03012222", "Xburewala", 5000)
    h = Hourly(1, "mahnoor", "36600000", "03034444", "Xgujrat", 45, 10)
    c = Commission(3, "sidra", "366666666", "030232322", "lahore", 10000, 20)
    p.add_emp(s)
    p.add_emp(h)
    p.add_emp(c)
    t = p.total_pay()
    print("Total weekly pay is: ", t)


main()


