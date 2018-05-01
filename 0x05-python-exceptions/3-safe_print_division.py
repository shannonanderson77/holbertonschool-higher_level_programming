#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return (None)
    finally:
        print("Inside result: {:.1f}".format(result))
        return (result)
