def safe_divide(numerator, denominator):
    try :
        quotient=float(numerator)/float(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        
    except ValueError:
        return "Error: Please enter numeric values only."
        
    else:
        print(" The result of the division is " ,end ="")
        return quotient
    