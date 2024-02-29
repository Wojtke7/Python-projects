inputs = eval(input())


def logging_decorator(function):
    def wrapper_func(*args):
        print(f"You called {function.__name__}({args[0]}, {args[1]}, {args[2]})")
        sum = 1
        for arg in args:
            sum *= arg
        print(f"It returned: {sum}")

    return wrapper_func


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
