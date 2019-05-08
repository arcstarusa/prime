#The block of code after the fist true condition (of an if or an elfif ) is executed.
# If none of the condition is true, the block of code after the else is exceuted.

x = 5
if x < 5:
    y = -1 #python uses indentation to delimit blocks
    z = 5
#elif and else clauses are optional
elif x > 5:
    y = 1
    z = 11
else:
    y = 0
    z = 10
print(x, y, z)

#the output would be 5 0 10