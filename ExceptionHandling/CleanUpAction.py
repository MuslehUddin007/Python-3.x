def divide(x,y):
    try:
        result = x//y
    except ZeroDivisionError as err:
        print("Sorry ! You are dividing by zero : ",err)
    else:
        print("Yeah ! Your answer is : ",result)
    finally:
        print("I'm finally clause, always raised !!")


divide(3,2)
divide(3,0)