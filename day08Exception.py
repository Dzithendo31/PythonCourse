def math_divide(a, b):
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("You cna't divide by Zero")
    else:
        # maybe you want to log somthing on the database
        print("Divison")
    finally:
        # When does, no matter if there is an erro or no errro we gonna run
        # We run Clean up code
        # Free up memory.
        print("Done")


# can we nest them
