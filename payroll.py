class Payroll:
    name = ""
    basicSalary = 0
    benefits = 0
    grossSalary = 0
    payee = 0
    nhif_deduct = 0
    nssf_deduct = 0
    net_taxable_income = 0
    netSalary = 0


    def __init__(self,n,bas,ben):
        Payroll.name = n
        Payroll.basicSalary = bas
        Payroll.benefits = ben
        Payroll.grossSalary (self)
        Payroll.payee (self)
        Payroll.nhif_deduct (self)
        Payroll.nssf_deduct (self)
        Payroll.net_taxable_income (self)
        Payroll.netSalary (self)
        Payroll.nssf_calc(self)
        Payroll.nhif_calc(self)


    def grossSalary_calc(self):
        self.grossSalary = self.basicSalary + self.benefits

    def nssf_calc(self):
        if self.grossSalary > 0 and self.grossSalary <= 6000:
            self.nssf_deduct = 6/100 * self.grossSalary
        elif self.grossSalary > 6000 and self.grossSalary <= 18000:
            self.nssf_deduct = 6/100 * self.grossSalary

""""Do taxable inoome here"""


    def nhif_calc(self):
        if self.grossSalary <= 5999:
             self.nhif_deduct = 150
        elif self.grossSalary >= 6000 and self.grossSalary <= 7999:
             self.nhif_deduct = 300
        elif self.grossSalary >= 8000 and self.grossSalary <= 11999:
             self.nhif_deduct= 400
        elif self.grossSalary >= 12000 and self.grossSalary <= 14999:
             self.nhif_deduct = 500
        elif self.grossSalary >= 15000 and self.grossSalary <= 15999:
             self.nhif_deduct = 600
        elif self.grossSalary >= 20000 and self.grossSalary <= 24999:
             self.nhif_deduct = 750
        elif self.grossSalary >= 25000 and self.grossSalary <= 29999:
             self.nhif_deduct = 850
        elif self.grossSalary >= 30000 and self.grossSalary <= 34999:
             self.nhif_deduct = 900
        elif self.grossSalary >= 35000 and self.grossSalary <= 39999:
             self.nhif_deduct = 950
        elif self.grossSalary >= 40000 and self.grossSalary <= 44999:
             self.nhif_deduct = 1000
        elif self.grossSalary >= 45000 and self.grossSalary <= 49999:
             self.nhif_deduct = 1100
        elif self.grossSalary >= 50000 and self.grossSalary <= 59999:
             self.nhif_deduct = 1200
        elif self.grossSalary >= 60000 and self.grossSalary <= 69999:
             self.nhif_deduct = 1300
        elif self.grossSalary >= 70000 and self.grossSalary <= 79999:
             self.nhif_deduct = 1400
        elif self.grossSalary >= 80000 and self.grossSalary <= 89999:
             self.nhif_deduct = 1500
        elif self.grossSalary >= 90000 and self.grossSalary <= 99999:
             self.nhif_deduct = 1600
        else:
            self.nhif_deduct = 1700

    def payee_calc(self):
        if self.grossSalary <= 12298:
            self.payee = self.grossSalary * 0.1
        elif self.grossSalary >= 12299 and self.grossSalary <= 23885:
            self.pa





    def netSalary_calc():
