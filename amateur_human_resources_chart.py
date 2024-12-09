employee_name = ["Tom", "Dick", "Harry"]
employee_surname = ["Perry", "Jones", "Potter"] 
employee_id = [122903, 593020, 432321 ]
employee_dob = ["10/05/2004", "03/30/1994", "07/22/1993"]
employee_age = ["age: 20", "age: 30", "age: 31"]
employee_address = ["561 Wallaby.St", "321 Decending.Ln", "123 Acending.Ln"]

def display_name(employee_name):
    first_name = employee_name
    return first_name

def display_surname(employee_surname):
    last_name = employee_surname
    return last_name

def display_empl_number(employee_id):
    id_numbers = employee_id
    return id_numbers

def display_dob(employee_dob):
    birthdate = employee_dob
    return birthdate

def display_age(employee_age):
    age_chart = employee_age
    return age_chart

def display_adress(employee_address):
    address_chart = employee_address
    return address_chart


print(display_name(employee_name))
print(display_surname(employee_surname))
print((display_empl_number(employee_id)))
print(display_dob(employee_dob))
print(display_age(employee_age))
print(display_adress(employee_address))
