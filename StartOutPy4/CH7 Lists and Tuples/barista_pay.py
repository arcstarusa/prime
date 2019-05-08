# This program calculates the gross pay for
# each of Megan's baristas.7-7

# NUM_EMPLOYEES is used as a constant for the
# size of the list.
NUM_EMPLOYEE = 6
def main():
    # Create list to hold employee hours.
    hours = [0] * NUM_EMPLOYEE

    # Get each employee's hours worked.
    for index in range(NUM_EMPLOYEE):
        print('Enter the hours worked by employee ', index + 1, ': ', sep='', end='')
        hours[index]=float(input())

    # Get the hourly pay rate.
    pay_rate = float(input('Enter the hourly pay rate: '))

    # Display each employee's gross pay.
    for index in range (NUM_EMPLOYEE):
        gross_pay = hours[index]*pay_rate
        print('Gross pay for employee ', index + 1, ': $', format(gross_pay, ',.2f'), sep='')

# Call the function
main()