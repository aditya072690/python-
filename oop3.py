while True:
    try:
        base = int(input("Enter the base value: "))
        exponent = int(input("Enter the exponent value: "))
    except:
        print('Please enter a valid number.')
    else:
        break

power = base ** exponent
print("For base {0} and exponent {1}, the answer is: {2}".format(base,exponent,power))
