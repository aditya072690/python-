while True:
    try:
        num = int(input("Enter any number: "))
    except:
        print('Please enter a valid number.')
    else:
        break

for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
    