# The determine_comm_rate function accepts the
# amount of sales as an argument and returns the
# applicable commission rate.
def determine_comm_rate(sales):
    rate =0.0
    # Determine the commission rate.
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

# Return the commission rate.
return rate