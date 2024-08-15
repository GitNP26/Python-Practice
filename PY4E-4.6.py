
def computepay(hours, rate):
    try:
        if hours <= 40:
            pay = hours*rate

        else:
            bonusrate = rate * 1.5
            overtimehours = hours - 40
            pay = (hours*rate)+(bonusrate*overtimehours)
        return(pay)

    except:
        print('Error: Please enter numeric values in both inputs')

Johnsalary = computepay(50, 10)
print('Pay is ' + str(Johnsalary))