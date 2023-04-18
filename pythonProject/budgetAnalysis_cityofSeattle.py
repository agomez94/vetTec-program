import csv
# local is used to format numbers as currency strings
import locale
# locale module is already pre=installedin  python
# here ill set the locale to the current system locale which has all categories
locale.setlocale(locale.LC_ALL, "")
class Department:
    department: str
    bcl: str
    program: str
    _2012_actual: int
    def __init__(self, department, bcl, program, _2012_actual):
        self.department = department
        self.bcl = bcl
        self.program = program
        self._2012_actual = _2012_actual


# parse_department_total() is a function that reads data from a CSV file,
# creates a list of Department objects, and returns the list.

def parse_department_total():
    filename = "city-of-seattle-2012-expenditures-dollars.csv"
    with open(filename) as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        # here is where im going to start the dictionary with 'department_dict = {}
        department_dict = {}
        for row in reader:
            department, bcl, program, _, _2012_actual, *_ = row
            if _2012_actual != '':
                #this will convert the dollar amount to float
                _2012_actual = locale.atof(_2012_actual)
                # if department in
                if department in department_dict:
                    department_dict[department].append(_2012_actual)
                else:
                    department_dict[department] = [_2012_actual]
        return department_dict


department_dict = parse_department_total()
for department, expenses in department_dict.items():
    # calculate the total expenses for the department and format it as
    # a currency string using the user's default settings
    total_spent = locale.currency(sum(expenses), grouping=True)
    print(f"Department: {department}, Total Funds Spent: {total_spent}")



# By Angel Gomez JR
#
#
# References:
#
# For Formatting -- https://stackabuse.com/format-number-as-currency-string-in-python/
# For Locale -- https://docs.python.org/3/library/locale.html
# Using atof -- https://stackoverflow.com/questions/48843193/convert-a-number-using-atof
# For locale.currency -- https://docs.python.org/3/library/locale.html#locale.currency