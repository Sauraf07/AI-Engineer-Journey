'''Task 3: Age Calculator Using Datetime
Objective

Work with datetime module.'''



from datetime import datetime


def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age
