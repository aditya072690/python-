'''
@author: 20124051 Aditya Chauhan
@description: Program No. -

Write a program to input roll no, student name, marks of physics, chemistry and maths out of 100. (0-100). Calculate total, percentage, calculate STATUS (pass, fail) if students scores above 40 in all the 3 subjects the STATUS should be pass otherwise fail. Calculate GRADE if STATUS is pass. Grade must be based on percentage value.

if percentage is above 70, then grade must be DISTINCTION

if percentage is above 60, then grade must be FIRST CLASS

if percentage is above 50, then grade must be SECOND CLASS

if percentage is above 40, then grade must be PASS CLASS
'''

print('Please enter you Enrollment number and Name: ')
while True:
    try:
        id = int(input('Enrollment id: \n'))
    except:
        print("Alphabets or Special characters are not allowed in Enrollment Id.")
    else:
        break

while (len(str(id)) != 8):
    print('Please enter a valid Enrolment Id: ')
    id = int(input('Enrollment id: \n'))

name = input('Name: \n')


def validate(subject):
    while (subject not in range(0, 101)):
        print("Please enter valid marks\n")
        subject = int(input())
    validate.condition = True
    validate.export = subject
    return subject


print("Please enter your marks for following subjects: \n")

try:
    maths = int(input('Maths: \n'))
except:
    print("Alphabets or Special characters are not allowed.")
    maths = int(input('Maths: \n'))

validate(maths)
if validate.condition == True:
    maths = validate.export

try:
    physics = int(input('Physics: \n'))
except:
    print("Alphabets or Special characters are not allowed.")
    physics = int(input('Physics: \n'))

validate(physics)
if validate.condition == True:
    physics = validate.export

try:
    chemistry = int(input('Chemistry: \n'))
except:
    print("Alphabets or Special characters are not allowed.")
    chemistry = int(input('Chemistry: \n'))

validate(chemistry)
if validate.condition == True:
    chemistry = validate.export
total = maths + physics + chemistry
percentage = (total * 100) / 300


def calstatus():
    if (maths > 40 and physics > 40 and chemistry > 40):
        calstatus.status = 'Pass'
    else:
        calstatus.status = 'Fail'

    return calstatus.status


def calgrade():
    if calstatus.status == 'Pass':
        if percentage > 40:
            calgrade.grade = 'PASS CLASS'
            if percentage > 50:
                calgrade.grade = 'SECOND CLASS'
                if percentage > 60:
                    calgrade.grade = 'FIRST CLASS'
                    if percentage > 70:
                        calgrade.grade = 'DISTINCTION'
        return calgrade.grade
    else:
        calgrade.grade = 'You have failed in one or more than one subject(s).\nTherefore your grade cannot be calculated.'
        return calgrade.grade


calstatus()
calgrade()

print()
print()
print("Enrollment Id:", id)
print("Name:", name)
print()
print('Marks:')
print('Maths:', maths)
print('Physics:', physics)
print('Chemistry:', chemistry)
print('Percentage: {0:.2f}%'.format(percentage))
print('Grade:', calgrade.grade)
