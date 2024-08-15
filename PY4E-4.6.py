
def computepay(hours, rate):
    """
    This function calculates pay by multiplying hours by rate
    For every hour over 40, rate is multiplied by 1.5.
    Parameters:
    hour (int): number of hours worked
    rate (int): the hourly rate of pay

    Returns:
    pay(int): This is the total pay for rate by hours worked
    """
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