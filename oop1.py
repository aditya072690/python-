print('Please enter you Enrollment number and Name: ')
id = int(input('Enrollment id: \n'))
while (len(str(id)) != 8):
    print('Plese enter a valid Enrolment Id: ')
    id = int(input('Enrollment id: \n'))
name = input('Name: \n')

def validate(subject):
    while (subject not in range(0,101)):
        print("Please enter valid marks\n")
        subject = int(input())
    validate.condition = True
    validate.export = subject
    return subject

print("Please enter your marks for following subjects: \n")

maths = int(input('Maths: \n'))
validate(maths)
if validate.condition == True:
    maths = validate.export


physics = int(input('Physics: \n'))
validate(physics)
if validate.condition == True:
    physics = validate.export


chemistry = int(input('Chemistry: \n'))
validate(chemistry)
if validate.condition == True:
    chemistry = validate.export
total = maths + physics + chemistry
percentage = (total * 100)/300


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
print("Enrollment Id:",id)
print("Name:",name)
print()
print('Marks:')
print('Maths:',maths)
print('Physics:',physics)
print('Chemistry:',chemistry)
print('Percentage: {0}%'.format(percentage))
print('Grade:',calgrade.grade)
