#the while loop is executed as long as the condition (which here is x > y) is true:

#This is a shorthand notation.
#Here, u an v are assigned a value of 0, x is set to 100, and y obtains a value of 30.
u, v, x, y = 0, 0, 100, 30
while x > y: #Loop block
    u = u + y
    x = x - y
    if x < y + 2:
        x = v + x
        x = 0
    else:
        v = v + y + 2
        x = x - y - 2
#It can contain a break (which ends the loop) and
#continue statements (which abort the current iteration of loop)
print(u, v)

# output is 60 32