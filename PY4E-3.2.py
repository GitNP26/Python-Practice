try:
    hours = float(input('Enter Hours\n'))
    rate = float(input('Enter Rate\n'))

    if hours <= 40:
        pay = hours*rate

    else:
        bonusrate = rate * 1.5
        overtimehours = hours - 40
        pay = (hours*rate)+(bonusrate*overtimehours)
    print('Pay is', pay)

except:
    print('Error: Please enter numeric values in both inputs')