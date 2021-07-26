from datetime import date


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

# Driver code

age =48
if age<10:
    print('error')


