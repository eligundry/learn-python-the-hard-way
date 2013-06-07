def add(a, b):
    print "ADD\t%d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUB\t%d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MUL\t%d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIV\t%d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(20, 2)
height = subtract(78, 10)
weight = multiply(25, 5)
iq = divide(260, 2)

print """
Age: %d
Height: %d
Weight: %d
IQ: %d
""" % (age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes %d. Can you do it by hand?" % what
