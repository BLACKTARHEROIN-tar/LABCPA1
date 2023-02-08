

def taxfuntion(salary):
    salaryMO = salary/12
    if float(salary) <= 250000:
         tax = float(salary)*0
         taxMo = float(tax)/12
         return "Annual Tax is: " + str(tax) + "\nMonthly tax is: " + str(taxMo)
    elif 400000 >= float(salary) > 250000:
         tax = float(salary)*0.15
         taxMo = tax/12
         return "Annual Tax is: " + str(tax) + "\nMonthly tax is: " + str(taxMo)
    elif 800000 >= float(salary) > 400000:
         tax = float(salary)*0.15
         taxMo = tax/12
         return "Annual Tax is: " + str(tax) + "\nMonthly tax is: " + str(taxMo)
    elif 2000000 >= float(salary) > 800000:
         tax = float(salary)*0.15
         taxMo = tax/12
         return "Annual Tax is: " + str(tax) + "\nMonthly tax is: " + str(taxMo)
    elif 8000000 >= float(salary) > 2000000:
         tax = float(salary)*0.15
         taxMo = tax/12
         return "Annual Tax is: " + str(tax) + "\nMonthly tax is: " + str(taxMo)
    elif 8000000 > float(salary): 
         tax = float(salary)*0.15
         taxMo = tax/12
         return "Annual Tax is: " + str(tax) + "\nMonthly tax is: " + str(taxMo)
     
salary = float(input("What's your annual salary: "))
taxStatement = taxfuntion(salary)
print(taxStatement)
