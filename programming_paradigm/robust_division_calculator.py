def safe_divide(numerator, denominator):
    try :
        quotient=float(numerator)/float(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return
    except ValueError:
        print("Error: Please enter numeric values only.")
        return
    else:
        print(" The result of the division is {}".format(quotient))
    