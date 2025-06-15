def safe_divide(numerator,denominator):
    try:
        float(numerator)
        float(denominator)
        
        if denominator == 0:
            raise ZeroDivisionError


    except ValueError:
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    else:
        return f"The result of the division is {float(numerator) / float(denominator)}"