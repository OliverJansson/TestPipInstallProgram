# Simple Calculater, attraction, subtraction, multiplication and division

def attraction(a:float,b:float):
    #Adds a and b together.
    c = a+b
    return(c)

def subtraction(a:float,b:float):
    #subtracts b from a.
    c = a-b
    return(c)

def multiplication(a:float,b:float):
    #Multiply a and b.
    c = a*b
    return(c)

def division(a:float,b:float):
    #divide a by b.
    try:    # Error handling if divition by 0
        c = a/b
        return(c)
    except Exception as Error:
        return(print(Error))
